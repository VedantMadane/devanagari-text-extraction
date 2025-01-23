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
pdf_path = "D:\Projects\hindi-text\\antarnad\"
create_folder_if_not_exists(pdf_path)
