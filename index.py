#!/usr/bin/python3
from fileOperations import getFileContent

print("Content-Type: text/html\n")
print(getFileContent("header.html"))
content = getFileContent("navigation.html")
content2 = getFileContent("login.html")
sp = content.split('<div id="">\n')
print(('<div id="logbar">\n' + content2 + '\n').join(sp))
print(getFileContent("registration.html"))
print(getFileContent("footer.html"))
