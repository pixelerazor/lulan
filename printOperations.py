from fileOperations import getFileContent

def printHeader():
    print("Content-Type: text/html\n")
    print(getFileContent("header.html"))

def printNav():
    content = getFileContent("navigation.html")
    content2 = getFileContent("login.html")
    sp = content.split('<div id="">\n')
    print(('<div id="logbar">\n' + content2 + '\n').join(sp))

def printSite():
    print(getFileContent("registration.html"))

def printFooter():
    print(getFileContent("footer.html"))
