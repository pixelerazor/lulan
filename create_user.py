#!/usr/bin/python3

import os # Debug related
import cgi # For getting form input

print("Content-type: text/html\n\n")

# Get input into dictionary
form = cgi.FieldStorage()

# Something wrong with input, return and modify input fields
# TODO: check if username is taken in DB?
if ("nickName" not in form) or ("password1" not in form) or ("password2" not in form) or (form["password1"].value != form["password2"].value):
    # Get index file for editing
    file = open("registration.html", "r")
    content = file.read()
    file.close()
    # Add error message before input form
    sp = content.split("<form")
    content = "\t\t<p>Fehlende oder falsche Eingabe!</p>\n<form".join(sp)
    # Error for missing nickName
    if ("nickName" not in form):
        sp = content.split("Benutzername")
        content = "FEHLT: Benutzername".join(sp)
    # Fill in nickName if found
    else:
        sp = content.split('name="nickName"')
        new = 'name="nickName" value="'+form["nickName"].value+'"'
        content = new.join(sp)
    # Same if/else routine for firstName and lastName
    if ("firstName" in form):
        sp = content.split('name="firstName"')
        content = ('name="firstName" value="'+form["firstName"].value+'"').join(sp)
    if ("lastName" in form):
        sp = content.split('name="lastName"')
        content = ('name="lastName" value="'+form["lastName"].value+'"').join(sp)
    # Passwords are there but differ, print an error in the placeholder
    if (("password1" in form) and ("password2" in form)) and (form["password1"].value != form["password2"].value):
        sp = content.split('placeholder="Passwort"')
        content = 'placeholder="FEHLER: Ungleiches Passwort"'.join(sp)
        sp = content.split('placeholder="Passwort wiederholen"')
        content = 'placeholder="FEHLER: Ungleiches Passwort"'.join(sp)
    # Mark passwords as missing in placeholder or input the given value
    else:
        if ("password1" not in form):
            sp = content.split('placeholder="Passwort"')
            content = 'placeholder="FEHLT: Passwort"'.join(sp)
        else:
            sp = content.split('name="password1"')
            new = 'name="password1" value="'+form["password1"].value+'"'
            content = new.join(sp)
        if ("password2" not in form):
            sp = content.split('placeholder="Passwort wiederholen"')
            content = 'placeholder="FEHLT: Passwort wiederholen"'.join(sp)
        else:
            sp = content.split('name="password2"')
            new = 'name="password2" value="'+form["password2"].value+'"'
            content = new.join(sp)
    print(content)
# Input valid, create the user
# TODO: write to DB instead of HTML
else:
    print("<p>")
    print("Benutzer angelegt: "+form["nickName"].value+"<br>\n")
    print("Passwort: "+form["password1"].value+"<br>\n")
    if "firstName" in form:
        print("Vorname: "+form["firstName"].value+"<br>\n")
    else:
        print("Kein Vorname<br>\n")
    if "lastName" in form:
        print("Nachname: "+form["lastName"].value+"</p>\n")
    else:
        print("Kein Nachname<br>\n")
    print("</p>")

# Debug
"""print("\n<br>\n<br>\n<font size=+1>Environment</font>\n<br>\n")
for param in os.environ.keys():
    print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))"""
