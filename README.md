# 🖼️ Photo Segregator using OCR

This Python automation script uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) to scan images from a folder and separate them into two categories:
- **Document Images** (with readable text)
- **Non-Document Images** (with little or no text)

It uses `pytesseract` and `OpenCV` to detect text from images and segregates them based on a defined threshold.

---

## 📌 Features

- Automatically scans all supported image formats from a given folder
- Detects presence of text using OCR
- Segregates images into:
  - `documents_folder/` if text is found
  - `non_documents_folder/` if not

---

## 📂 How to Use

### 1. Install Dependencies

```bash
pip install pytesseract opencv-python

```
Also, download and install Tesseract OCR on your system.

### 2. Set Up

Make sure you update the script with:

    Correct path to your Tesseract installation

    Correct input_folder, documents_folder, and non_documents_folder paths

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

### 3. Run the Script
python coder.py
