import re
import sys
from lxml import etree


def group_surfaces_by_leaf(input_file, output_file):
    NS_URL = "http://www.tei-c.org/ns/1.0"
    NS = "{" + NS_URL + "}"

    parser = etree.XMLParser(remove_blank_text=False, strip_cdata=False)

    try:
        tree = etree.parse(input_file, parser)
        root = tree.getroot()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    surface_parents = set(node.getparent() for node in root.iter(f"{NS}surface"))

    for parent in surface_parents:
        new_children = []

        current_grp = None
        current_leaf_number = None

        original_children = list(parent)

        for node in original_children:
            if node.tag == f"{NS}surface":
                n_attr = node.get("n", "")

                match = re.match(r"^(\d+)", n_attr)

                if match:
                    leaf_num = match.group(1)

                    if leaf_num != current_leaf_number:
                        current_leaf_number = leaf_num

                        current_grp = etree.Element(f"{NS}surfaceGrp")
                        current_grp.set("n", f"f{leaf_num}")
                        current_grp.set("type", "leaf")

                        new_children.append(current_grp)

                    current_grp.append(node)

                else:
                    current_leaf_number = None
                    current_grp = None
                    new_children.append(node)

            else:
                if current_grp is not None:
                    current_grp.append(node)
                else:
                    new_children.append(node)

        for child in list(parent):
            parent.remove(child)

        for child in new_children:
            parent.append(child)

    tree.write(output_file, encoding="UTF-8", xml_declaration=True, pretty_print=False)
    print(f"Successfully processed. Output saved to: {output_file}")


if __name__ == "__main__":
    input_filename = "../voynichMS_TEST.xml"
    output_filename = "../voynichMS_grouped.xml"

    if len(sys.argv) > 1:
        input_filename = sys.argv[1]
    if len(sys.argv) > 2:
        output_filename = sys.argv[2]

    group_surfaces_by_leaf(input_filename, output_filename)