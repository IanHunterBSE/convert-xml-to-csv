#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
tree = ET.ElementTree(file='/Users/andreaks/berlin_1279_2.xml')
elem = tree.getroot()
print elem.tag, elem.attrib

for child_of_elem in elem:
    print child_of_elem.tag, child_of_elem.attrib
