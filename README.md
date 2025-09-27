# Hover Cell Segmentation & Density Map Generator

This repository provides tools for processing **whole-slide images (WSIs)** and segmentation outputs to generate **cell density maps** and **cell-type specific arrays**.  
It integrates preprocessing, segmentation polygon normalization, and visualization for tumor microenvironment analysis.

---

## 📌 Features
- Reads WSIs (`.svs`) and segmentation files from HoverNet-like outputs.  
- Normalizes cell contour polygons across different magnifications.  
- Generates **cell-type specific arrays**:
  - Neoplastic cells
  - Inflammatory cells
  - Connective tissue cells
  - Epithelial cells
  - Dead cells  
- Produces **density heatmaps** for visualization.  
- Supports **20X** and **40X** magnification.

---

## 📂 Project Structure
# Input directories
wsi_dir: "/path/to/wsi/files"            # Directory with .svs whole slide images
mask_dir: "/path/to/mask/files"          # Directory with mask .png files
hover_dir: "/path/to/segmentation/files" # Directory with segmentation results

# File settings
suffix: ".png"   # Mask file extension
mpp: 40          # Magnification (20 or 40)

# Output directories
out_array: "read_array"   # Folder for density arrays (CSV)
out_map: "read_map"       # Folder for density maps (PNG)

python main.py

# Configuration file for Tumor-TIL Map Generator

# Input: array directory generated from HoverNet density pipeline
arr_dir: "read/hovernet_20x_array"

# Output: directory for tumor–TIL visualization maps
out_dir: "read_tumorTIL"

python gen_map.py
