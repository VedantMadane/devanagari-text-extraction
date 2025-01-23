from pdf2image import convert_from_path

# Loop through each image and save it with a sequential filename
# for volume:
    # Specify the path to your PDF file
pdf_names = ['jan_1996', 'jun_1996', 'mar_1996', 'may_1996', 'diwali_1996_part1']
for pdf_name in pdf_names:
    pdf_path = filepath = f"D:\Projects\hindi-text\\antarnad\\{pdf_name}.pdf"
# Convert the PDF to images (all pages by default)
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save(f"D:/Projects/hindi-text/antarnad/{pdf_name}/page_{i+1}.jpg", "JPEG")  # Adjust filename format as needed

print("PDF successfully converted to images!")