from bs4 import BeautifulSoup
from copy import copy

with open('../../xml/graphics.xml', 'r', encoding='utf-8') as file:
    graphic_elements_xml = file.read()

with open('../../ZL3b-n_test2.xml', 'r', encoding='utf-8') as file:
    target_xml = file.read()


def merge_xml():
    graphics_soup = BeautifulSoup(graphic_elements_xml, 'xml')
    target_soup = BeautifulSoup(target_xml, 'xml')

    # This will find all 227 <graphic> elements
    graphics_list = graphics_soup.find_all('graphic')
    surfaces_list = target_soup.find_all('surface')

    print(f"Found {len(graphics_list)} graphics and {len(surfaces_list)} target surfaces")

    for i in range(min(len(graphics_list), len(surfaces_list))):
        # Copy the graphic element before inserting
        graphic_copy = copy(graphics_list[i])
        surfaces_list[i].insert(0, graphic_copy)

    with open('../ZL3b-n_test3.xml', 'w', encoding='utf-8') as file:
        file.write(str(target_soup))


if __name__ == "__main__":
    merge_xml()