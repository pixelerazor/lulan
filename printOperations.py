from fileOperations import getFileContent

def indentNewlines(code, num=0):
    sp = code.split("\n")
    code = (num*"    ")+(("\n"+(num*"    ")).join(sp))
    return code[0:-(num*4)]

def printHeader(ind=0):
    print("Content-Type: text/html\n")
    print("<!DOCTYPE html>")
    print(getFileContent("header.html"), end='')

def printNav(ind=0):
    content = getFileContent("navigation.html")
    content2 = indentNewlines(getFileContent("login.html"), 2) # Add two indentations two match navgigation.html
    sp = content.split('<div id="">\n')
    print(indentNewlines(('<div id="logbar">\n' + content2).join(sp), 3), end='') # Add three indentations two match header.html

def printSite(ind=0):
    print(indentNewlines(getFileContent("registration.html"), 3), end='') # Add three indentations two match header.html

def printFooter(ind=0):
    print(getFileContent("footer.html"), end='')
