import json
import re

def parse_shuowen_jiezi_to_json(input_file_path, output_file_path):
    pattern = r'^(\d+)\s(\S+?):\s(\S+?)[\uff1a](.*)'

    characters_data = []
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                id, radical, character, explanation = match.groups()
                if len(character) == 1:
                    explanation = explanation.replace('\n', ' ').strip()  # Replace newline characters with spaces and strip
                    character_info = {
                        'id': int(id),
                        'radical': radical,
                        'character': character,
                        'explanation': explanation
                    }
                    characters_data.append(character_info)

    # Save the intermediate results to a JSON file
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(characters_data, json_file, ensure_ascii=False, indent=4)

    return output_file_path

input_file_path = 'shuowen_jiezi_full.txt'
output_file_path = 'shuowen_jiezi.json'

parse_shuowen_jiezi_to_json(input_file_path, output_file_path)
