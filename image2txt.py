from pdf2image import convert_from_path
import pytesseract

# Assuming you have converted the PDF to images using the previous approach

# Set Tesseract's path (replace with your actual path if different)
pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract.exe'  # Windows
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
  text = pytesseract.image_to_string(image_path, config='--oem 1 --psm 6')
  return text

# Loop through each image and extract text
for i, image in enumerate(images):
  image_path = f"page_{i+1}.jpg"  # Assuming filenames from previous conversion
  hindi_text = extract_hindi_text(image_path)
  print(f"Extracted text from page {i+1}:\n {hindi_text}")
