import json
import os
import xml.etree.ElementTree as ET

def char_to_utf8_hex(c):
    return c.encode('utf-8').hex()

# Load the JSON data
with open('gb2312_characters_test.json', 'r') as file:
    data = json.load(file)

# Ensure the 'dist' directory exists
os.makedirs('dist', exist_ok=True)

# Load the SVG template
with open('template.svg', 'r') as file:
    svg_template = file.read().replace('\n', '').replace('\t', '')

# Generate SVG images and save them to the 'dist' directory
for number, item in enumerate(data):
    # Replace placeholders in the SVG template with actual data
    svg_modified = svg_template.replace('{{char}}', item)
    svg_modified = svg_modified.replace('{{utf8Hex}}', char_to_utf8_hex(item))

    # Parse the modified SVG
    tree = ET.ElementTree(ET.fromstring(svg_modified))

    # Save the modified SVG
    output_path = os.path.join('dist', f"{number}.svg")
    
    # Write the SVG file
    with open(output_path, 'w') as f:
        f.write(ET.tostring(tree.getroot(), encoding='unicode').replace('ns0:',''))

print("ok")
