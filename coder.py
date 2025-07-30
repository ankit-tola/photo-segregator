import os
import cv2
import pytesseract
import shutil

#  Set the path to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#  Input: Folder with all your photos (change this!)
input_folder = r"D:\dad\wp image in phone(!sorting)"

#  Output folders for separation
documents_folder = r"D:\dad\image whatsapp-1"
non_documents_folder = r"D:\dad\image wp -2"

#  Threshold: Number of detected characters to treat as a "document"
text_threshold = 15

#  Create output folders if they don't exist
os.makedirs(documents_folder, exist_ok=True)
os.makedirs(non_documents_folder, exist_ok=True)

# Supported image types
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.webp']

#  Process all images
print(" Scanning photos...")

for filename in os.listdir(input_folder):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f" Skipping unreadable file: {filename}")
            continue

        # Convert to grayscale for better OCR accuracy
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Extract text using OCR
        text = pytesseract.image_to_string(gray)

        # Decide destination based on detected text
        if len(text.strip()) > text_threshold:
            print(f" Writing found in: {filename}")
            shutil.copy2(image_path, os.path.join(documents_folder, filename))
        else:
            print(f" No writing: {filename}")
            shutil.copy2(image_path, os.path.join(non_documents_folder, filename))

print(" All done! Your photos have been separated.")
