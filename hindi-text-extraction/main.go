package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	// Define the directory containing the text files
	dir := "D:\\Projects\\hindi-text\\nothing"

	// Create or open the output file
	outputFile, err := os.Create("combined.txt")
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}
	defer outputFile.Close()

	// Create a buffered writer for efficient writing
	writer := bufio.NewWriter(outputFile)

	// Iterate through the specified range of files
	for i := 2; i <= 177; i++ {
		// Construct the filename
		filename := fmt.Sprintf("page_%d.txt", i)
		filepath := filepath.Join(dir, filename)

		// Open each text file
		inputFile, err := os.Open(filepath)
		if err != nil {
			fmt.Printf("Error opening file %s: %v\n", filepath, err)
			continue // Skip to the next file if there's an error
		}

		// Read the contents of the file and write to the output file
		scanner := bufio.NewScanner(inputFile)
		for scanner.Scan() {
			_, err := writer.WriteString(scanner.Text() + "\n")
			if err != nil {
				fmt.Println("Error writing to output file:", err)
				break
			}
		}

		// Check for errors during scanning
		if err := scanner.Err(); err != nil {
			fmt.Printf("Error reading from file %s: %v\n", filepath, err)
		}

		// Close the input file after processing
		inputFile.Close()
	}

	// Flush any buffered data to the output file
	if err := writer.Flush(); err != nil {
		fmt.Println("Error flushing writer:", err)
	}

	fmt.Println("All files combined successfully into combined.txt")
}
