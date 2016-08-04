#!/usr/bin/python3

print("Content-Type: text/html\n")
file = open("index.html", "r")
content = file.read()
print(content)
