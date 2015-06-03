#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys
import codecs

tree = ET.parse('/Users/andreaks/berlin_1306.xml')
elem = tree.getroot()

import sys
f = codecs.open('/Users/andreaks/berlin_1306.csv', 'w', encoding="utf-8")
sys.stdout = f

for child_of_elem in elem:
    print child_of_elem.text,";",
