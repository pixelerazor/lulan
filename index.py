#!/usr/bin/python3
import os
import re
from fileOperations import getFileContent

print("Content-Type: text/html\n")

print(getFileContent("header.html"))
"""uri = os.environ["REQUEST_URI"]
site = re.findall("site=(\w*)", uri, re.ASCII)
if site != []:
    site = site[0]
else:
"""
content = getFileContent("navigation.html")
content2 = getFileContent("login.html")
sp = content.split('<div id="">\n')
print(('<div id="logbar">\n' + content2 + '\n').join(sp))
print(getFileContent("registration.html"))

print(getFileContent("footer.html"))
