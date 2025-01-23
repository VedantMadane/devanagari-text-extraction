import easyocr # type: ignore
import os
folder_path = 'D:\Projects\hindi-text\parv'
def create_file_with_folder(filepath):
  """
  Creates the file if it doesn't exist, creating any necessary directories.

  Args:
      filepath (str): Path to the file including directory.
  """

  # Get directory path from the file path
  directory = os.path.dirname(filepath)

  # Create the directory structure (including parent directories) if it doesn't exist
  os.makedirs(directory, exist_ok=True)

  # Open the file for writing, creating it if necessary
  with open(filepath, "w") as the_file:
    # Write your content here
    the_file.write("This is some content for the new file.")
def count_image_files(folder_path):
  """
  Counts image files (common extensions) in a folder.

  Args:
      folder_path (str): Path to the folder.

  Returns:
      int: Number of image files found.
  """

  image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]  # Common image extensions
  image_count = 0

  for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):  # Check for files only
      extension = os.path.splitext(filename)[1].lower()  # Get lowercase extension
      if extension in image_extensions:
        image_count += 1

  return image_count

image_count = count_image_files(folder_path)

print(f"Number of image files in '{folder_path}': {image_count}")

append_result = []
reader = easyocr.Reader(['mr', 'en', 'hi']) # this needs to run only once to load the model into memory
while 1==1:
    for i in range(1, image_count):  # Loop from page_1 to page_632
        filename = f"{folder_path}\page_{i}.jpg"
    #image_path = os.path.join(image_folder, filename)
        arrayOfStrings = reader.readtext(filename, detail = 0)
        result = " ".join(arrayOfStrings)
        append_result.append(result)
        print(result)

        create_file_with_folder('D:\\Projects\\hindi-text\\parv\\1\\1.txt')
        with open(f"{os.path.dirname(folder_path)}\1\\1.txt", "w",  encoding="utf-8") as text_file:
            text_file.writelines(str(result))
        print(result, f"Text written to output of page {i}")
        # text_file.close()
    with open(f'D:\Projects\hindi-text\parv\{os.path.basename(folder_path)}_1.txt', "a",  encoding="utf-8") as combined_text:
        combined_text.writelines(str(append_result))
    print("Text written to output.txt!")

import os

import 

# # Example usage
# filepath = "D:\\Projects\\hindi-text\\antarnad\\output\\apr_1996.txt"
# create_file_with_folder(filepath)

# print(f"File created: {filepath}")

def functionToConcatenateString():
    my_list = ["This", "is", "a", "list", "of", "strings"]
    joined_string = ""
    let = []
    for element in my_list:
        joined_string += element + " "
    joined_string = joined_string[:-1]  # Remove extra space at the end
    print(joined_string)
    return joined_string