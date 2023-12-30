import json
import os
import xml.etree.ElementTree as ET

def char_to_utf8_hex(c):
    return c.encode('utf-8').hex()

# Load the JSON data
with open('shuowen_jiezi_test.json', 'r') as file:
    data = json.load(file)

# Ensure the 'dist' directory exists
os.makedirs('dist', exist_ok=True)

# Generate SVG images and save them to the 'dist' directory
for item in data:
    # Load the SVG template
    with open('template.svg', 'r') as file:
        svg_template = file.read()

    # Replace placeholders in the SVG template with actual data
    svg_modified = svg_template.replace('{{char}}', item['character'])
    svg_modified = svg_modified.replace('{{utf8Hex}}', char_to_utf8_hex(item['character']))

    # Parse the modified SVG
    tree = ET.ElementTree(ET.fromstring(svg_modified))

    # Save the modified SVG
    output_path = os.path.join('dist', f"{item['id']}.svg")
    tree.write(output_path)

# Variables to output
svg_files_generated = [os.path.join('dist', f"{item['id']}.svg") for item in data]
