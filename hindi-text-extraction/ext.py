import pytesseract
from pdf2image import convert_from_path
import glob
filepath = "D:\Projects\hindi-text\antarnad"
pdfs = glob.glob(filepath)

for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500)
    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='Devanagari')

        with open(f'{pdf_path}.txt', 'a') as the_file:
            the_file.write(text)