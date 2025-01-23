import io
from pdfminer.high_level import extract_text

def convert_pdf_to_text(pdf_file):
  """
  Extracts text from a PDF file using pdfminer.six.

  Args:
    pdf_file: Path to the PDF file.

  Returns:
    Extracted text content from the PDF file.
  """
  text = ""
  with open(pdf_file, 'rb', encoding="utf-8") as f:
    output = io.StringIO()
    extract_text(f, output)
    text = output.getvalue()
    with open(filename, "w") as text_file:
       text_file.write(text)
       print(f"Text saved to: {filename}")
  return text

# Extracted text can be used to create a docx or other document format using libraries like python-docx (manual formatting adjustments might be needed).
pdf_file = "D:/Documents/readingMaterial/rising/2015.66526.Hints-For-Self-culture.pdf"
filename = "D:/Documents/readingMaterial/rising/hints.txt"
convert_pdf_to_text(pdf_file)
# Open the file in write mode ("w") and write the text content

