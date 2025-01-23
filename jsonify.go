// MAHARISHI UNIVERSITY OF MANAGENENT स्वर्गारोहण्पर्व [Mahabharata] VEDIC LITERATURE COLLECTION तेषु भास्वरदेहेषु पुण्याभिजनकर्मसु समागतेषु देवेषु व्यगमत्तत्तमो नृप ३ नादृश्यन्त च तास्तत्र यातनाः पापकर्मिणाम् नदी वैतरणी चैव कूटशाल्मलिना सह ४ लोहकुम्भ्यः शिलाश्चैेव नादृश्यन्त भयानकाः विकृतानि शरीराणि यानि तत्र समन्ततः ददर्श राजा कौन्तेयस्तान्यदृश्यानि चाभवन् ५ ततो वायुः सुखस्पर्शः पुण्यगन्धवहः शिवः ववौ देवसमीपस्थः शीतलोउतीव भारत ६ मरुतः सह शक्रेण वसवश्चाश्विनौ सह साध्या रुद्रास्तथादित्या ये चान्येउपि दिवौकसः ७ सर्वे तत्र समाजग्मुः सिद्धाश्च परमर्षयः यत्र राजा महातेजा धर्मपुत्रः स्थितोउभवत् = ततः शक्रः सुरपतिः श्रिया परमया युतः युधिष्ठिरमुवाचेदं सान्त्वपूर्वमिदं वचः ६ युधिष्ठिर महाबाहो प्रीता देवगणास्तव एह्येहि पुरुषव्याघ्र कृतमेतावता विभो सिद्धिः प्राप्ता त्वया राजल्लोकाश्चाप्यच्तयास्तव १० नच मन्युस्त्वया कार्यः शृणु चेदं वचो मम त्रवश्यं नरकस्तात द्रष्टव्यः सर्वराजभिः ११ शुभानामशुभानां च द्वौ राशी पुरुषर्षभ यः पूर्वं सुकृतं पश्चान्निरयमेति सः नरकभाग्यस्तु पश्चात्स्वर्गमुपैति सः १२ भूयिष्ठं पापकर्मा यः स पूर्वं स्वर्गमश्नुते तेन त्वमेवं गमितो मया श्रेयोर्थिना नृप १३ व्याजेन हि त्वया द्रोण उपचीर्णः सुतं प्रति व्याजेनैव ततो राजन्दर्शितो नरकस्तव १४ यथैव त्वं तथा भीमस्तथा पार्थो यमौ तथा द्रौपदी च तथा कृष्णा व्याजेन नरकं गताः १५ त्रागच्छ नरशार्दूल मुक्तास्ते चैव किल्विषात् 5489 भुङ्क्ते पूर्वं
// Input will be a txt file with the string above inside it
// We will read the file and jsonify the string and write it to a new file
// Output will be a json file with the string above inside it
// The json file will have the following structure
// {
// "3":"तेषु भास्वरदेहेषु पुण्याभिजनकर्मसु समागतेषु देवेषु व्यगमत्तत्तमो नृप
// }"
// We will use the encoding/json package to encode the data
// We will use the os package to read and write the file
package main

import (
	"encoding/json"
	"io/ioutil"
	"regexp"
	"strings"
)

func convertToJSON(text string) (map[string]string, error) {
	// Regular expression to match numeric keys including ५, ६, ७, etc.

	re := regexp.MustCompile(`[\p{N}]+`)

	// Split text into lines
	lines := strings.Split(text, "\n")

	// Initialize result map
	result := make(map[string]string)

	// Track current key and value
	var currentKey string
	var currentValueLines []string

	for _, line := range lines {
		// Check if line starts with a numeric key
		matches := re.FindStringSubmatch(line)
		if matches != nil {
			// Save previous key-value pair if exists
			if currentKey != "" {
				result[currentKey] = strings.TrimSpace(strings.Join(currentValueLines, " "))
			}

			// Reset for new key
			currentKey = matches[1]
			currentValueLines = []string{strings.TrimSpace(line[len(matches[0]):])}
		} else if currentKey != "" {
			// Accumulate value lines
			currentValueLines = append(currentValueLines, strings.TrimSpace(line))
		}
	}

	// Add last key-value pair
	if currentKey != "" {
		result[currentKey] = strings.TrimSpace(strings.Join(currentValueLines, " "))
	}

	return result, nil
}

func main() {
	// Read input file
	content, err := ioutil.ReadFile("D:\\Projects\\devanagari-text-extraction\\data\\processed\\page11.txt")
	if err != nil {
		panic(err)
	}

	// Convert to JSON
	jsonData, err := convertToJSON(string(content))
	if err != nil {
		panic(err)
	}

	// Write JSON to file
	outputJSON, err := json.MarshalIndent(jsonData, "", "  ")
	if err != nil {
		panic(err)
	}

	err = ioutil.WriteFile("D:\\Projects\\devanagari-text-extraction\\data\\processed\\output.json", outputJSON, 0644)
	if err != nil {
		panic(err)
	}
}
