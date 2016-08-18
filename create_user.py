#!/usr/bin/python3

import os # Debug related
import cgi # For getting form input
from printOperations import *
from create_user_games import *

# Get input into dictionary
form = cgi.FieldStorage()

# Something wrong with input, return and modify input fields
# TODO: check if username is taken in DB?
if ("nickName" not in form) or ("password1" not in form) or ("password2" not in form) or (form["password1"].value != form["password2"].value):
    printHeader()
    printNav()
    # Get index file for editing
    file = open("html/registration.html", "r")
    content = file.read()
    file.close()
    # Add error message before input form
    sp = content.split("<form")
    content = "\t\t<h3>Input missing or wrong!</h3>\n<form".join(sp)
    # Error for missing nickName
    if ("nickName" not in form):
        sp = content.split("Nickname ...")
        content = "MISSING: Nickname".join(sp)
    # Fill in nickName if found
    else:
        sp = content.split('name="nickName"')
        content = ('name="nickName" value="'+form["nickName"].value+'"').join(sp)
    # Same if/else routine for firstName and lastName
    if ("firstName" in form):
        sp = content.split('name="firstName"')
        content = ('name="firstName" value="'+form["firstName"].value+'"').join(sp)
    if ("lastName" in form):
        sp = content.split('name="lastName"')
        content = ('name="lastName" value="'+form["lastName"].value+'"').join(sp)
    # Passwords are there but differ, print an error in the placeholder
    if (("password1" in form) and ("password2" in form)) and (form["password1"].value != form["password2"].value):
        sp = content.split('placeholder="Password ..."')
        content = 'placeholder="ERROR: Passwords differ"'.join(sp)
        sp = content.split('placeholder="Repeat Password ..."')
        content = 'placeholder="ERROR: Passwords differ"'.join(sp)
    # Mark passwords as missing in placeholder or input the given value
    else:
        if ("password1" not in form):
            sp = content.split('placeholder="Password ..."')
            content = 'placeholder="MISSING: Password ..."'.join(sp)
        else:
            sp = content.split('name="password1"')
            new = 'name="password1" value="'+form["password1"].value+'"'
            content = new.join(sp)
        if ("password2" not in form):
            sp = content.split('placeholder="Repeat password ..."')
            content = 'placeholder="MISSING: Repeat password ..."'.join(sp)
        else:
            sp = content.split('name="password2"')
            new = 'name="password2" value="'+form["password2"].value+'"'
            content = new.join(sp)
    print(content)
    printFooter()
# Input valid, create the user
# TODO: write to DB instead of HTML
else:
    printHeader()
    printNav()
    print("<p>")
    print("Benutzer angelegt: "+form["nickName"].value+"<br>\n")
    print("Passwort: "+form["password1"].value+"<br>\n")
    if "firstName" in form:
        print("Vorname: "+form["firstName"].value+"<br>\n")
    else:
        print("Kein Vorname<br>\n")
    if "lastName" in form:
        print("Nachname: "+form["lastName"].value+"\n")
    else:
        print("Kein Nachname<br>\n")
    print("</p>")
    gamesHtml()
    printFooter()
