from PIL import Image
import pytesseract
import os
import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext('chinese.jpg', detail = 0)
def extract_hindi_text(image_path):
  """
  Extracts Hindi text from an image using Tesseract OCR.

  Args:
      image_path: Path to the image file.

  Returns:
      Extracted Hindi text as a string.
  """
  # Use config='--oem 1 --psm 6' for better Hindi text extraction
  text = pytesseract.image_to_string(image_path, config='--oem 1 --psm 6', lang='Devanagari')
  return text.strip()  # Remove leading/trailing whitespaces

# Specify the folder containing the images
image_folder = "D:\Projects\hindi-text\vol1"

# Open the output text file in append mode
with open("extracted_text.txt", "a") as text_file:

  # Loop through all files in the folder (assuming numerical order)
  for i in range(1, 633):  # Loop from page_1 to page_632
    filename = f"page_{i}.jpg"
    image_path = os.path.join(image_folder, filename)

    # Extract text
    hindi_text = extract_hindi_text(image_path)

    # Append extracted text to the file (add newline for clarity)
    if hindi_text:
      text_file.write(f"Page {i}:\n{hindi_text}\n\n")
      print(f"Extracted text from page {i}")

print("Text extraction completed!")
