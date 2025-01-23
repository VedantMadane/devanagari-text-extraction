import glob

def get_all_pdfs(directory):
  """
  Gets all PDF files from a specified directory.

  Args:
      directory (str): Path to the directory containing PDFs.

  Returns:
      list: List of paths to the PDF files.
  """

  # Use glob.glob with "*.pdf" pattern to match all PDF files
  pdf_paths = glob.glob(f"{directory}/*.pdf")
  return pdf_paths

# Example usage
directory = "D:\Projects\hindi-text\\sanskrit"
pdf_files = get_all_pdfs(directory)

if pdf_files:
  print("Found PDFs:")
  for pdf_path in pdf_files:
    print(pdf_path)
else:
  print("No PDF files found in the specified directory.")

import os

def create_folder_if_not_exists(pdf_path):
  """
  Creates a folder with the same name as the PDF if it doesn't exist.

  Args:
      pdf_path (str): Path to the PDF file.
  """

  # Get the folder path based on the PDF path
  folder_path = os.path.dirname(pdf_path)

  # Get the PDF filename without extension
  filename, _ = os.path.splitext(os.path.basename(pdf_path))

  # Create the folder if it doesn't exist
  folder_to_create = os.path.join(folder_path, filename)
  if not os.path.exists(folder_to_create):
    os.makedirs(folder_to_create)
    print(f"Created folder: {folder_to_create}")

# Example usage
#pdf_path = "D:\Projects\hindi-text\\antarnad\"


for i in pdf_files:
  create_folder_if_not_exists(i)
  