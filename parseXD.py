import xml.etree.ElementTree as ET
import re

# https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2
# for movie in root.findall("./genre/decade/movie/[year='1992']"):
# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
# root.find("./genre[@category='Action']/decade[@years='2000s']")

class XMLParse():

    def __init__(self, filename):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

    def printXML(self,node):
        print(ET.tostring(node).decode("utf-8"))

    def printXMLs(self,nodes):
        for node in nodes:
            print(ET.tostring(node).decode("utf-8"))

    def printRoot(self):
        print(self.root.tag)

    def printFirstsChilds(self):
        for child in self.root:
            print(child.tag, child.attrib)

    def printTagsANDAtributes(self):    
        print([elem.tag for elem in self.root.iter()])

    # "./genre/decade/movie/format"
    def findAll(self,pattern):
        nodes = self.root.findall(pattern)
        return nodes

    # "./genre/decade/movie/format"
    def getKeys(self,pattern):
        for child in self.root.findall(pattern):
            print(child.tag)
    
    def getValues(self,pattern):
        for child in self.root.findall(pattern):
            print(child.text)    

    def setAttributeIfTextMatch(self,where, what, attrib, ifmatch_value, ifnot_value):
        # "./genre/decade/movie/format"
        nodes = self.root.findall(where)
        for form in nodes:
            # Search for the what in the format text
            match = re.search(what,form.text)
            if match:
                form.set(attrib, ifmatch_value)
            else:
                form.set(attrib, ifnot_value)
        return nodes

    def saveXML(self,name):
        self.tree.write(name)
        
    def addTag(self,xpath, name_newtag):
        # "./genre[@category='Action']"
        node = self.root.find(xpath)
        new_tag = ET.SubElement(action, name_newtag)
        return node

    def addAttribute(self,xpath, attr_name, attr_value):
        node = self.root.find(xpath)
        node.attrib[attr_name] = attr_value
        return node

    def removeByXpath(self,xpath):
        node = self.root.find(xpath)
        self.root.remove(node)
        return node

    def removeAll(self,xpath):
        nodes = self.root.findall(xpath)
        for node in nodes:
            self.root.remove(node)
        return nodes