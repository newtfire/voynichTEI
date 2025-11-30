from lxml import etree
import re



# Your sample TEI data

with open('../voynichMS_TEST.xml', 'r', encoding="utf-8") as file:
    xml_data = file.read()

def process_tei_hands(xml_string):
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(xml_string.encode('utf-8'), parser)

    # 2. Define the Namespace
    # TEI uses a specific namespace that we must use to find elements
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

    # 3. Define the Regex to find the hand
    # Looking for: "Currier's language [Letter], hand [Number]"
    pattern = re.compile(r"Currier'?s language [AB], +hand (\d)\??")

    # 4. Iterate over every <surface> element
    for surface in root.findall('.//tei:surface', namespaces=ns):
        found_hand = None

        # Look specifically for comments inside this surface
        # xpath('./comment()') finds all direct child comments
        for comment in surface.xpath('./comment()'):
            if comment.text:
                match = pattern.search(comment.text)
                if match:
                    # We found the hand number (e.g., "2")
                    found_hand = match.group(1)
                    break  # Stop looking at comments for this surface

        # 5. If a hand was found, apply it to all <zone> children
        if found_hand:
            zones = surface.findall('tei:zone', namespaces=ns)
            for zone in zones:
                zone.set('hand', f"#{found_hand}")

    # 6. Return the modified XML as a string
    return etree.tostring(root, encoding='unicode', pretty_print=True)


# Run the function
new_xml = process_tei_hands(xml_data)


# Optional: Save to a file
with open("output_voynich.xml", "w", encoding="utf-8") as f:
    f.write(new_xml)