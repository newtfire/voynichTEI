# Merged XML Processing Script
# 1. Groups surfaces by folio and adds hand/language attributes to zones
# 2. Inserts graphic elements into surface elements

import re
import os
from bs4 import BeautifulSoup
from copy import copy


def process_voynich_xml(xml_content):
    """
    Groups <surfaceGrp> by folio number and adds xml:lang and hand attributes to <zone>
    """
    # Regex to capture each <surface> block and identify the folio number
    surface_pattern = re.compile(r'(<surface\s+n="f(\d+)[^"]*".*?</surface>)', re.DOTALL)

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
            wrapper = f'<surfaceGrp n="{folio_num}" type="leaf">\n{combined_surfaces}\n</surfaceGrp>'
            output_parts.append(wrapper)
            seen_folios.add(folio_num)

        last_end = end

    # Append any remaining text after the final surface
    output_parts.append(xml_content[last_end:])
    return "".join(output_parts)


def merge_graphics(graphics_xml_path, target_xml_content):
    """
    Merges <graphic> elements from graphics.xml into <surface> elements
    """
    with open(graphics_xml_path, 'r', encoding='utf-8') as file:
        graphic_elements_xml = file.read()

    graphics_soup = BeautifulSoup(graphic_elements_xml, 'xml')
    target_soup = BeautifulSoup(target_xml_content, 'xml')

    # Find all <graphic> elements and <surface> elements
    graphics_list = graphics_soup.find_all('graphic')
    surfaces_list = target_soup.find_all('surface')

    print(f"Found {len(graphics_list)} graphics and {len(surfaces_list)} target surfaces")

    # Insert graphics into surfaces
    for i in range(min(len(graphics_list), len(surfaces_list))):
        graphic_copy = copy(graphics_list[i])
        surfaces_list[i].insert(0, graphic_copy)

    return str(target_soup)


def main():
    # File paths
    input_file = '../../ZL3b-n_test1.xml'
    output_file = '../../ZL3b-n_test2.xml'
    graphics_file = '../../xml/graphics.xml'

    try:
        print("Processing XML file...")

        # Check if input files exist
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"The file {input_file} was not found.")
        if not os.path.exists(graphics_file):
            raise FileNotFoundError(f"The file {graphics_file} was not found.")

        # Read input file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()

        # Step 1: Process folio grouping and zone attributes
        print("Step 1: Processing folio groups and zone attributes...")
        processed_xml = process_voynich_xml(data)
        print("  ✓ Hand/Language attributes injected into <zone> tags")
        print("  ✓ Surfaces grouped into <surfaceGrp> by folio number")

        # Step 2: Merge graphics
        print("\nStep 2: Merging graphic elements...")
        final_xml = merge_graphics(graphics_file, processed_xml)

        # Save final output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_xml)

        print(f"\n✓ All processing complete! Output saved to {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()