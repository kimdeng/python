#/usr/bin/python
import re


with open(r'character.txt','r') as text:
    
    a = "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text.read()))

print a
