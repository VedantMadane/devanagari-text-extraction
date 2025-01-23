import os

def combine_text_files(folder_path, output_file):
  """
  Combines all text files in a folder into a single output file.

  Args:
      folder_path: The path to the folder containing the text files.
      output_file: The path to the output file where the combined text will be saved.
  """
  text_files = []
  for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Filter for .txt files
      full_path = os.path.join(folder_path, filename)
      text_files.append(full_path)

  if not text_files:
    print(f"No text files found in folder: {folder_path}")
    return

  with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in text_files:
      try:
        with open(filename, 'r', encoding='utf-8') as infile:
          content = infile.read()
          outfile.write(content)
          outfile.write('\n')  # Add a newline character between files
      except FileNotFoundError:
        print(f"Error: File not found: {filename}")

# Example usage
folder_path = 'D:\Projects\hindi-text\output\khanda1'  # Replace with your folder path
output_file = 'D:\Projects\hindi-text\output\khanda1combined.txt'

combine_text_files(folder_path, output_file)

print(f"Files in folder combined successfully: {output_file}")
