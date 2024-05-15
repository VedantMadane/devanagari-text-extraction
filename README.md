# devanagari-text-extraction

1. Take a PDF and separate each page into a jpeg
2. Take each jpeg and extract the text on it
3. Write the text into text file with the name of the jpeg
4. After the text in all jpegs has been written into their corresponding text files, combine the text files into a single text file with the name of the PDF after ordering the text files in the order of occurance of the page-wise jpegs in the PDF:
   `find . -type f -name "*.txt" -print0 | sort -zV | xargs -0 cat > combinedInOrder.txt`
6. Do steps 1 to 4 for each PDF in the folder.
