import xml.etree.ElementTree as ET

def GenerateXML(filename):
    root = ET.Element("Catalog")

    m1 = ET.Element('mobile')
    root.append(m1)

    b1 = ET.SubElement(m1, 'brand')
    b1.text ="Redmi"

    tree = ET.ElementTree(root)

    with open(filename, 'wb') as files:
        tree.write(files)

if __name__=="__main__":
    GenerateXML("Catalog.xml")