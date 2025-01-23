import pytesseract
import os
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files (x86)\Tesseract-OCR"
from pdf2image import convert_from_path
import glob
filepath = "D:/Projects/hindi-text/vol1.pdf"
pdfs = glob.glob(filepath)

for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 1)
    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='hindi')
        with open(f'{pdf_path}.txt', 'a') as the_file:
            the_file.write(text)