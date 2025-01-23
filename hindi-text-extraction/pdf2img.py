import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(filepath, page_count=None):
  """
  Extracts text from a PDF file using Tesseract OCR.

  Args:
      filepath (str): Path to the PDF file.
      page_count (int, optional): Number of pages to extract text from.
          If None, extracts text from all pages. Defaults to None.

  Returns:
      str: The extracted text from the PDF file.
  """

  # Ensure Tesseract is installed and configured (adjust paths if needed)
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

  # Handle invalid file paths or non-PDF files gracefully
  if not filepath.endswith(".pdf"):
    print("Error: Invalid file format. Please provide a PDF file.")
    return ""

  try:
    # Convert PDF to images
    images = convert_from_path(filepath, dpi=200)  # Adjust DPI if needed

    # Extract text from each image using Tesseract OCR with Devanagari language
    extracted_text = ""
    for i, image in enumerate(images):
      if page_count is not None and i >= page_count:
        break  # Stop processing if page limit reached
      text = pytesseract.image_to_string(image, lang='Devanagari')
      extracted_text += text + "\n\n"  # Add newlines between pages

    return extracted_text

  except Exception as e:
    print(f"Error: An error occurred while processing the PDF: {e}")
    return ""

# Get user input for file path and optional page count
file_path = input("Enter the path to the PDF file: ")
page_count_str = input("Enter the number of pages to extract (optional, enter 'all' for all pages): ")

try:
  page_count = int(page_count_str) if page_count_str.lower() != "all" else None
except ValueError:
  print("Invalid page count. Please enter a number or 'all'.")
  page_count = None

# Extract text from the PDF
extracted_text = extract_text_from_pdf(file_path, page_count)

if extracted_text:
  print("Extracted text:\n")
  print(extracted_text)
else:
  print("No text extracted. Please check for errors or invalid file.")
