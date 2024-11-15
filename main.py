import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('sample.xml')
root = tree.getroot()

# Find specific tags and print their text
nam = root.find('nam')  # Finds the <nam> tag inside the root element
ph = root.find('ph')    # Finds the <ph> tag inside the root element
mail=root.find('mail')

# Print the values of <nam> and <ph>
#Name
if nam is not None:
    print(f"Name: {nam.text}")
else:
    print("Tag <nam> not found.")

#Phone
if ph is not None:
    print(f"Phone: {ph.text}")
else:
    print("Tag <ph> not found.")

#Mail
if mail is not None:
    print(f"Mail: {mail.text}")
else:
    print("Tag <mail> not found.")