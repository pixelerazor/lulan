from fileOperations import getFileContent
import asyncio
import websockets

def indentNewlines(code, num=0):
    sp = code.split("\n")
    code = (num*"    ")+(("\n"+(num*"    ")).join(sp))
    return code[0:-(num*4)]

def getIndentLevel(content):
    if (content[-1] == " "):
        cur = 1
        ind = 0
        while (content[-cur] == " "):
            ind += 1
            cur += 1
        if (ind > 0):
            return int(ind / 4)
        else:
            return 0
    elif (content[-1] == "\n"):
        cur = content[:-1].rfind("\n")
        ind = 0
        while content[cur+1] == " ":
            ind += 1
            cur += 1
        if (ind > 0):
            return int(ind / 4)
        else:
            return 0
    else:
        return 0

def printHeader():
    print("Content-Type: text/html\n")
    #print("<!DOCTYPE html>")
    header = getFileContent("html/header.html")
    print(header, end='')
    return getIndentLevel(header)

def printFooter():
    print(getFileContent("html/footer.html"), end='')

# TODO: load another top right menu when logged in
def printNav(indent=0):
    content = getFileContent("html/navigation.html")
    sp = content.split('<!-- menu -->\n')
    indent1 = getIndentLevel(sp[0])
    content2 = indentNewlines(getFileContent("html/login.html"), indent1)
    print(indentNewlines((content2).join(sp), indent), end='')
    return indent

def printSite(args, indent=0):
    site = ""
    if "site" not in args.keys() or args["site"].value == "registration":
        # when not logged in:
        print(indentNewlines(getFileContent("html/registration.html"), indent), end='') # Add three indentations to match header.html
        return indent
    else:
        site = args["site"].value
    if site == "chat":
        name = ""
        if "name" not in args.keys():
            name = "anon"
        else:
            name = args["name"].value
        if "message" in args.keys():
            async def hello():
                async with websockets.connect('ws://localhost:8001') as websocket:
                    await websocket.send((name + "," + args["message"].value))
            asyncio.get_event_loop().run_until_complete(hello())
        content = getFileContent("html/chat.html")
        print(indentNewlines((content.replace("{}", name)), indent), end='')
