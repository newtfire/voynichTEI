import xml.etree.ElementTree as ET

# If you have the data in a file named 'data.xml'
# tree = ET.parse('data.xml')
# root = tree.getroot()

# For this example, we'll parse the string directly

with open('../voynichMS_TEST.xml', 'r', encoding='utf-8') as file:
    xml_data = file.read()

try:
    root = ET.fromstring(xml_data)

    # Use './/graphic' to find all graphic tags at any depth
    graphics = root.findall(".//{*}graphic")

    print(f"Found {len(graphics)} graphic elements:\n")

    for i, graphic in enumerate(graphics, 1):
        # Get the 'url' attribute from the tag
        url = graphic.get('url')
        print(f'<graphic url="{url}"/>')

except ET.ParseError as e:
    print(f"Error parsing XML: {e}")