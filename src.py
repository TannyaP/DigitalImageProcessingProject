import os
import numpy as np
import spectral as spy
import matplotlib.pyplot as plt

# 1. Paths
base_dir = r"C:\NADIA\SEM5\Digital Image Processing\PROJECT\ML"
output_dir = os.path.join(base_dir, "Processed_Reflectance")
os.makedirs(output_dir, exist_ok=True)

# Spoilage-sensitive band
spoilage_band = 70    

# 2. Process each paneer folder
for folder_name in os.listdir(base_dir):

    folder_path = os.path.join(base_dir, folder_name)
    if not os.path.isdir(folder_path):
        continue

    capture_path = os.path.join(folder_path, "capture")
    if not os.path.exists(capture_path):
        continue

    # Find HDR files
    hdr_files = [f for f in os.listdir(capture_path) if f.lower().endswith(".hdr")]

    scene_hdr = dark_hdr = white_hdr = None

    for f in hdr_files:
        name = f.upper()
        if "DARK" in name:
            dark_hdr = os.path.join(capture_path, f)
        elif "WHITE" in name:
            white_hdr = os.path.join(capture_path, f)
        else:
            scene_hdr = os.path.join(capture_path, f)

    # Skip if any file missing
    if not (scene_hdr and dark_hdr and white_hdr):
        print(f"Skipping {folder_name} (missing scene/dark/white HDR)")
        continue

    print(f"\nProcessing folder: {folder_name}")

    
    # 3. Load scene, dark, white & compute reflectance
    scene = spy.open_image(scene_hdr).load().astype(np.float32)
    dark  = spy.open_image(dark_hdr).load().astype(np.float32)
    white = spy.open_image(white_hdr).load().astype(np.float32)

    reflectance = (scene - dark) / (white - dark + 1e-6)
    reflectance = np.clip(reflectance, 0, 1)

    # Save reflectance cube (.npy)
    cube_path = os.path.join(output_dir, f"{folder_name}_reflectance.npy")
    np.save(cube_path, reflectance)
    print("Saved reflectance cube →", cube_path)

    # 4. Extract spoilage band (70) — but DO NOT use band in filename
    band_idx = min(spoilage_band, reflectance.shape[2] - 1)

    img = reflectance[:, :, band_idx]
    img = (img - img.min()) / (img.max() - img.min() + 1e-6)

    # FINAL OUTPUT FILE — clean name, without "band70"
    out_png = os.path.join(output_dir, f"{folder_name}_spoilage_map.png")
    plt.imsave(out_png, img, cmap="jet")

    print(f"Saved spoilage visualization → {out_png}")

print("\ All folders processed successfully!")




