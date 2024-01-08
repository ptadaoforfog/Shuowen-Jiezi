from fontTools.ttLib import TTFont
import json

# Path to the font file
font_file_path = 'fangsong_GB2312.ttf'
output_json_path = 'chinese_characters.json'

# Load the font file
font = TTFont(font_file_path)

# Extract Chinese characters from the font file
chinese_characters = []
for table in font['cmap'].tables:
    for char_code in table.cmap.keys():
        if 0x4E00 <= char_code <= 0x9FFF:
            chinese_characters.append(chr(char_code))

# Convert the list of characters to JSON format with UTF-8 encoding
json_data = json.dumps(chinese_characters, ensure_ascii=False)

# Save the JSON data to a file
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

# Result variables
font_file_path, output_json_path, json_data
