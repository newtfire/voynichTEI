import xml.etree.ElementTree as ET

# 1. Define a custom TreeBuilder to capture comments
# This ensures comments are treated as nodes in the tree, preventing them from being stripped.
class CommentedTreeBuilder(ET.TreeBuilder):
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)

def update_voynich_urls(input_file, output_file):
    # 2. Register the TEI namespace
    namespace = "http://www.tei-c.org/ns/1.0"
    ET.register_namespace('', namespace)

    # 3. Parse the XML file using the Custom Builder
    # We pass our custom builder to the XMLParser
    parser = ET.XMLParser(target=CommentedTreeBuilder())
    tree = ET.parse(input_file, parser=parser)
    root = tree.getroot()

    # 4. Define the counter and base URL structure
    current_id = 1006254
    base_url_template = "https://collections.library.yale.edu/iiif/2/{}/full/full/0/default.jpg"

    # 5. Find all 'graphic' elements and update them
    graphic_tag = f"{{{namespace}}}graphic"

    count = 0
    for graphic in root.iter(graphic_tag):
        # Generate the new URL with the current ID
        new_url = base_url_template.format(current_id)

        # Set the new url attribute
        graphic.set('url', new_url)

        # Increment the ID for the next image
        current_id += 1
        count += 1

    # 6. Save the modified file
    tree.write(output_file, encoding='UTF-8', xml_declaration=True)
    print(f"Success! Updated {count} graphic elements.")
    print(f"File saved as: {output_file}")


# Run the function
if __name__ == "__main__":
    update_voynich_urls('../temp.xml', '../voynich_updated2.xml')