import os
import re

def combine_text_files_in_order(folder_path, output_file):
  """
  Combines text files named page_1.txt to page_632.txt in a folder into a single output file, preserving order.

  Args:
      folder_path: The path to the folder containing the text files.
      output_file: The path to the output file where the combined text will be saved.
  """
  text_files = []
  # Pattern to match filenames (replace if naming convention differs)
  page_pattern = r'^page(\d+)OfKhanda1.txt$'

  for filename in os.listdir(folder_path):
    if not os.path.isfile(os.path.join(folder_path, filename)):
      continue  # Skip non-files

    match = re.match(page_pattern, filename)
    if match:
      # Extract page number from filename (assuming numbering starts from 1)
      page_number = int(match.group(1))
      text_files.append((page_number, filename))  # Tuple with (page number, filename)

  # Sort files based on page number
  text_files.sort(key=lambda x: x[0])

  if not text_files:
    print(f"No text files matching the pattern found in folder: {folder_path}")
    return

  with open(output_file, 'w') as outfile:
    for page_number, filename in text_files:
      full_path = os.path.join(folder_path, filename)
      try:
        with open(full_path, 'r') as infile:
          content = infile.read()
          outfile.write(content)
          outfile.write('\n')  # Add a newline character between files
          print(f"Pages in folder combined successfully: {output_file}")

      except FileNotFoundError:
        print(f"Error: File not found: {filename}")

# Example usage
folder_path = 'D:\Projects\hindi-text\output\khanda1\\'  # Replace with your folder path
output_file = 'D:\Projects\hindi-text\output\inOrderKhanda1combined.txt'

combine_text_files_in_order(folder_path, output_file)

