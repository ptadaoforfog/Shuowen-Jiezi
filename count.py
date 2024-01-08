import json

# Function to validate the 'character' field in each entry
def validate_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    entries = []
    for entry in data:
        entries.append(entry)
            
    return entries

# Path to the JSON file
json_file_path = 'gb2312_characters.json'

# Call the validate function and store the invalid entries
entries = validate_json(json_file_path)

# Output the invalid entries
print(len(entries))
