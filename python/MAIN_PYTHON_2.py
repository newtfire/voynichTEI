# Use this Python File Second
# Gets xml:lang and hand attributes for <zone>
# Groups <surfaceGrp> by folio number

import re
import os
from xml.dom import minidom


def process_voynich_xml(xml_content):
    # Regex to capture each <surface> block and identify the folio number
    surface_pattern = re.compile(r'(<surface\s+n="f(\d+)[^"]*">.*?</surface>)', re.DOTALL)

    # Find Language and Hand in notes within the surface
    lang_pattern = re.compile(r"Language\s+([AB])", re.IGNORECASE)
    hand_pattern = re.compile(r"hand\s+([1-5])", re.IGNORECASE)

    all_matches = list(surface_pattern.finditer(xml_content))
    if not all_matches:
        return xml_content

    groups = {}
    for match in all_matches:
        full_surface = match.group(1)
        folio_num = match.group(2)

        # Extract language and hand info from the current surface text
        lang_match = lang_pattern.search(full_surface)
        hand_match = hand_pattern.search(full_surface)

        lang_val = lang_match.group(1).upper() if lang_match else None
        hand_val = hand_match.group(1) if hand_match else None

        # Build attribute string for <zone>
        attr_string = ""
        if hand_val:
            attr_string += f' hand="#scribe{hand_val}"'
        if lang_val:
            attr_string += f' xml:lang="{lang_val}"'

        # Put into every <zone> tag in this surface
        if attr_string:
            full_surface = full_surface.replace('<zone>', f'<zone{attr_string}>')

        if folio_num not in groups:
            groups[folio_num] = []
        groups[folio_num].append(full_surface)

    output_parts = []
    last_end = 0
    seen_folios = set()

    for match in all_matches:
        start, end = match.span()
        folio_num = match.group(2)

        # Append the original text found between surfaces
        output_parts.append(xml_content[last_end:start])

        # If this is the first time we've encountered this folio group (e.g. '1'),
        # insert the entire <surfaceGrp> block.
        if folio_num not in seen_folios:
            combined_surfaces = "\n".join(groups[folio_num])
            wrapper = f'<surfaceGrp n="{folio_num}">\n{combined_surfaces}\n</surfaceGrp>'
            output_parts.append(wrapper)
            seen_folios.add(folio_num)

        last_end = end

    # Append any remaining text after the final surface
    output_parts.append(xml_content[last_end:])
    return "".join(output_parts)

input = '../ZL3b-n_test1.xml'
output = '../ZL3b-n_test2.xml'

try:
    if not os.path.exists(input):
        raise FileNotFoundError(f"The file {input} was not found.")

    with open(input, 'r', encoding='utf-8') as f:
        data = f.read()

    processed_xml = process_voynich_xml(data)

    with open(output, 'w', encoding='utf-8') as f:
        f.write(processed_xml)

    print(f"Success: Processed XML saved to {output}")
    print("- Hand/Language attributes injected into <zone> tags.")
    print("- Surfaces grouped into <surfaceGrp> by folio number.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")