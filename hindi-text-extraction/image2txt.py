from pdf2image import convert_from_path
import pytesseract
import os

def get_all_image_paths(user_directory):
  image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]  # Common image extensions
  images = []

  for root, directories, filenames in os.walk(user_directory):
    for filename in filenames:
      if os.path.isfile(os.path.join(root, filename)):
        extension = os.path.splitext(filename)[1].lower()
        if extension in image_extensions:
          image_path = os.path.join(root, filename)
          images.append(image_path)

  return images

# Example usage (assuming user directory access is allowed)
user_directory = 'D:\Projects\hindi-text\\nothing'
images = get_all_image_paths(user_directory)

if images:
  print("Found image paths:")
  for image_path in images:
    print(image_path)
else:
  print("No image files found in the user directory or its subdirectories.")

# Assuming you have converted the PDF to images using the previous approach

# Set Tesseract's path (replace with your actual path if different)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'  # Windows
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Linux/macOS

def extract_hindi_text(image_path):
  """
  Extracts Hindi text from an image using Tesseract OCR.

  Args:
      image_path: Path to the image file.

  Returns:
      Extracted Hindi text as a string.
  """
  # Use config='--oem 1 --psm 6' for better Hindi text extraction
  text = pytesseract.image_to_string(image_path )
                                     #config='')
  return text

# Loop through each image and extract text
for i, image in enumerate(images):
  image_path = f"page_{i+1}.jpg"  # Assuming filenames from previous conversion
  hindi_text = extract_hindi_text(image_path)
  print(f"Extracted text from page {i+1}:\n {hindi_text}")