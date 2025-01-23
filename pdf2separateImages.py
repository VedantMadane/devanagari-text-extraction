from pdf2image import convert_from_path

# Loop through each image and save it with a sequential filename
# for volume:
    # Specify the path to your PDF file
pdf_path = filepath = f"D:\Projects\devanagari-text-extraction\data\\raw\\2.pdf"
# Convert the PDF to images (all pages by default)
images = convert_from_path(pdf_path)
for i, image in enumerate(images):
    image.save(f"D:\Projects\devanagari-text-extraction\data\\cleaned\\2page_{i:03d}.jpg", "JPEG")  # Adjust filename format as needed

print("PDF successfully converted to images!")