#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys
import codecs

tree = ET.parse('/file.xml')
elem = tree.getroot()

import sys
f = codecs.open('/file.csv', 'w', encoding="utf-8")
sys.stdout = f

for child_of_elem in elem:
    print child_of_elem.text,";",
