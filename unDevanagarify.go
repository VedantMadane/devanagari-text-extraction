package main

import (
	"fmt"
	"os"
)

func convertDevanagariToArabic(input string) string {
	devanagariMap := map[rune]rune{
		'०': '0',
		'१': '1',
		'२': '2',
		'३': '3',
		'४': '4',
		'५': '5',
		'६': '6',
		'७': '7',
		'८': '8',
		'९': '9',
	}

	var result []rune
	for _, char := range input {
		if arabicNum, exists := devanagariMap[char]; exists {
			result = append(result, arabicNum)
		} else {
			result = append(result, char)
		}
	}

	return string(result)
}

// Example usage
func main() {
	// Take input from txt file
	file, err := os.Open("D:\\Projects\\devanagari-text-extraction\\data\\processed\\page11.txt")
	converted := convertDevanagariToArabic(input)
	fmt.Println(converted) // Outputs: 567
}
