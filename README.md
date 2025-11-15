# 🧀 Paneer Contamination Detection Using Hyperspectral Imaging (HSI)

This repository presents our project on **detecting contamination in paneer samples using 80-band Hyperspectral Imaging (HSI)**.  
We replicate the workflow of the research paper *“Bread Contamination Detection using Deep Learning and Thermal Imaging”*, but enhance the methodology by replacing thermal imaging with **Hyperspectral Imaging**, enabling deeper spectral analysis and early detection of chemical/microbial changes.

---

## 📌 **Project Summary**

This project investigates contamination progression in paneer stored at room temperature.  
Hyperspectral imaging captures subtle variations caused by:

- **Acetic Acid**
- **Hydrogen Peroxide**
- **Natural spoilage**
- **Paneer type differences**

Our aim is to build a **non-destructive, data-driven contamination detection system** using spectral features and deep learning.

---

## 📂 **Dataset Overview**

### **Paneer Types**
- Milkymist Paneer  
- Malai Paneer  
- Tofu (Soy Paneer)

### **Treatment Variations**
1. Normal (Control)  
2. 6 drops Acetic Acid  
3. 3 drops Acetic Acid  
4. 6 drops Hydrogen Peroxide  
5. 3 drops Hydrogen Peroxide  

Each treatment contains **3 cubes**, captured from **2 sides**, across **multiple days**.

---

### **📷 Current Dataset Status**
- **140 Hyperspectral images** captured so far  
- Each image contains **~80 spectral bands (VIS–NIR)**  
- Images stored in `.hdr` format  
- Samples kept inside a **sealed box at room temperature**

### **🎯 Final Target Dataset**
- **540 images total** over a 6-day observation cycle

---

## 🧪 **Experimental Setup**

- Paneer cubes prepared and treated with chemical drops  
- Stored in a **sealed plastic box** at room temperature  
- Captured using an **80-band hyperspectral camera**  
- Consistent camera angle, lighting, and distance  
- **Dark and white reference images** recorded before every capture  
- Metadata logged for:
  - Paneer type  
  - Treatment  
  - Day & time  
  - Side  
  - Temperature & humidity  

---

## 🔍 **Work Completed So Far**

- Collected **140 HSI cubes**  
- Imported dataset into **Google Colab**  
- Visualized all **80 spectral bands**  
- Observed distinct spectral changes for:
  - Acid-treated samples  
  - Peroxide-treated samples  
  - Normal samples  
- Organized dataset with naming conventions & metadata  
- Prepared PCA/band-selection plans for RGB conversion  
- Wrote and finalized the IEEE research paper  

---

## 🎯 **Project Goals**

- Build a contamination-detection system using HSI  
- Extend base paper from thermal → hyperspectral imaging  
- Create annotated dataset for deep learning  
- Analyze spectral signatures across all 80 bands  
- Train YOLO models for contamination detection  
- Evaluate with precision, recall, and mAP  

---

## 🧭 **Future Work**

- Expand dataset to full **540 HSI images**  
- Perform **PCA** or **band selection**  
- Convert HSI → pseudo-RGB for YOLO  
- Annotate contamination regions  
- Train **YOLOv11n** and compare models  
- Compute performance metrics  
- Develop a real-time contamination detection pipeline  

---

## 📄 **Research Paper**

A complete IEEE-formatted research paper is included containing:

- Abstract  
- Keywords  
- Introduction & Motivation  
- Related Work  
- Proposed Methodology  
- Experimental Setup  
- Results & Discussion  
- Conclusion & Future Work  
- References  

---

## 👥 **Team**

- **Divya P**  
- **Nadia Naureen**  
- **Tannya Pasricha**

---

