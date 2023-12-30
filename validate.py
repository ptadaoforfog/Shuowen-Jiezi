import json

# Function to validate the 'character' field in each entry
def validate_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    invalid_entries = []
    for entry in data:
        if len(entry['character']) != 1:
            invalid_entries.append(entry)

    return invalid_entries

# Path to the JSON file
json_file_path = 'shuowen_jiezi.json'

# Call the validate function and store the invalid entries
invalid_entries = validate_json(json_file_path)

# Output the invalid entries
print(invalid_entries)
