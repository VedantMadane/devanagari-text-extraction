import PyPDF2
from docx import Document
from warnings import PendingDeprecationWarning
PendingDeprecationWarning = DeprecationWarning  # Assuming you only need PendingDeprecationWarning

def convert_pdf_to_docx(pdf_file, docx_file):
  """
  Converts a PDF file to a docx file.

  Args:
    pdf_file: Path to the PDF file.
    docx_file: Path to the output docx file.
  """
  text = ""
  with open(pdf_file, 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      text += page.extract_text()

  document = Document()
  document.add_paragraph(text)
  document.save(docx_file)

# Example usage
pdf_path = "D:/Documents/readingMaterial/rising/2015.66526.Hints-For-Self-culture.pdf"
docx_path = "D:/Documents/readingMaterial/rising/2015.66526.Hints-For-Self-culture.docx"
convert_pdf_to_docx(pdf_path, docx_path)
