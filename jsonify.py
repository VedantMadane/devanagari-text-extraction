import json
import re

def convert_to_json(text):
    # Regular expression to match numeric keys including ५, ६, ७, etc.
    pattern = re.compile(r'[\\d\u0966-\u096F]+')
    
    # Split text into lines
    lines = text.split('\n')
    
    # Initialize result dictionary
    result = {}
    
    # Track current key and value
    current_key = None
    current_value_lines = []
    
    for line in lines:
        # Check if line starts with a numeric key
        print("line\n", line)
        match = pattern.match(line)
        if match:
            print("match\n", match)
            # Save previous key-value pair if exists
            if current_key is not None:
                print(current_key, current_value_lines)
                result[current_key] = ' '.join(current_value_lines).strip()
            
            # Reset for new key
            current_key = match.group()
            current_value_lines = [line[match.end():].strip()]
            print(current_key, current_value_lines)
        elif current_key is not None:
            # Accumulate value lines
            print("current_key is not None\n", current_key)
            current_value_lines.append(line.strip())
    
    # Add last key-value pair
    if current_key is not None:
        result[current_key] = ' '.join(current_value_lines).strip()
    
    return result

def main():
    try:
        # Read input file
        with open(r"D:\\Projects\devanagari-text-extraction\data\\processed\\2page1.txt", 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Convert to JSON
        json_data = convert_to_json(content)
        
        # Write JSON to file
        with open(r"D:\\Projects\devanagari-text-extraction\data\\processed\\jsonify_op_from_py.json", 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
