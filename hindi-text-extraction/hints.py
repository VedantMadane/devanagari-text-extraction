import easyocr # type: ignore
append_result = []
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
while 1==1:
    for i in range(1, 376):  # Loop from page_1 to page_632
        filename = f"D:/Projects/hindi-text/nothing/page_{i+1}.jpg"
    #image_path = os.path.join(image_folder, filename)
        arrayOfStrings = reader.readtext(filename, detail = 0)
        result = " ".join(arrayOfStrings)
        append_result.append(result)
        print(result)
        with open(f"D:/Projects/hindi-text/nothing/page_{i+1}.txt", "a",  encoding="utf-8") as text_file:
            text_file.writelines(str(result))
        print(result, f"Text written to output of page {i}")
        # text_file.close()
    with open(f"D:\Projects\hindi-text\output\\nothing.txt", "a",  encoding="utf-8") as combined_text:
        combined_text.writelines(str(append_result))
    print("Text written to output.txt!")