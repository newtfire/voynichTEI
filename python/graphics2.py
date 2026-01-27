from bs4 import BeautifulSoup

with open('../xml/graphics.xml', 'r', encoding='utf-8') as file:
    graphic_elements_xml = file.read()

# 2. Your target XML structure (the pages you want to fill)
# I am using a simplified version for the example
with open('../ZL3b-n_test2.xml', 'r', encoding='utf-8') as file:
    target_xml = file.read()

def merge_xml():
    # Parse the snippets
    graphics_soup = BeautifulSoup(graphic_elements_xml, 'xml')
    target_soup = BeautifulSoup(target_xml, 'xml')

    # Get lists of both
    graphics_list = graphics_soup.find_all('graphic')
    surfaces_list = target_soup.find_all('surface')

    # Loop through them by index to pair them up
    for i in range(min(len(graphics_list), len(surfaces_list))):
        # Insert the graphic as the first child of the surface
        surfaces_list[i].insert(0, graphics_list[i])

    with open('../ZL3b-n_test3.xml', 'w', encoding='utf-8') as file:
        file.write(str(target_soup))

if __name__ == "__main__":
    merge_xml()