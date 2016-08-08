#!/usr/bin/python3

def getFileContent(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content
