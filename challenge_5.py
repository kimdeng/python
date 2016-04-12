#!/usr/bin/python

import re
import urllib

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

nothing = "12345"

search = re.compile(" (\d*)$")

search_html = re.compile("\.html$")

for i in xrange(400):
    print "%s: " % nothing,

    line = urllib.urlopen("%s%s" % (url,nothing)).read()
    print line 

    if search_html.findall(line):
        break


    match = search.findall(line)

    if match:
    
        nothing = match [0]
    else:
    
        nothing =str(int(nothing) / 2)
