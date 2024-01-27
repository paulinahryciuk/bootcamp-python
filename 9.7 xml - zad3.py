from xml.dom import minidom

DOMTree = minidom.parse('dane_xml.xml')
print(DOMTree.toxml())

cNodes = DOMTree.childNodes
print(cNodes)
print(cNodes[0])
