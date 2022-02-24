# Fill in this file with the code from parsing XML exercise
import xml.etree.ElementTree as ET
import re

#Open the xml
xml = ET.parse("myfile.xml")
#Associate root with the top of the xml tree structure
#Note:root is based on class xml.etree.ElementTree.Element 
root = xml.getroot()
print ("root type", type(root))

#print ("Root: ", root)
#Extract the name space field from the root.tag string
#group(0) contains just the matched string

ns = re.match('{.*}', root.tag).group(0)

#print ("NS: ", ns)


#Search for edit-config tag and prepend the ns 
editconf = root.find("{}edit-config".format(ns))
#Then find the next occurance of default-operation
defop = editconf.find("{}default-operation".format(ns))
#Then find the next occurance of test-operation
testop = editconf.find("{}test-option".format(ns))

print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))

