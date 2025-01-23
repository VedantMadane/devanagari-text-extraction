import easyocr # type: ignore
append_result = []
reader = easyocr.Reader(['mr', 'en', 'hi']) # this needs to run only once to load the model into memory
issue = 'jan_1996'#, 'jan_1996', 'jun_1996', 'mar_1996', 'may_1996', 'diwali_1996_part1'}
while 1==1:
    for i in range(1, 156):  # Loop from page_1 to page_632
        filename = f"D:\Projects\hindi-text\\antarnad\\{issue}\page_{i}.jpg"
    #image_path = os.path.join(image_folder, filename)
        arrayOfStrings = reader.readtext(filename, detail = 0)
        result = " ".join(arrayOfStrings)
        append_result.append(result)
        print(result)
        with open(f"D:\Projects\hindi-text\\antarnad\output\\{issue}\\{issue}.txt", "a",  encoding="utf-8") as text_file:
            text_file.writelines(str(result))
        print(result, f"Text written to output of page {i}")
        # text_file.close()
    with open(f"D:\Projects\hindi-text\output\\{issue}.txt", "a",  encoding="utf-8") as combined_text:
        combined_text.writelines(str(append_result))
    print("Text written to output.txt!")