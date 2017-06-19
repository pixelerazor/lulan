#!/usr/bin/python3

import os # Debug related
import cgi, sqlite3 # For getting form input
from printOperations import *

# Get input into dictionary
form = cgi.FieldStorage()

# get list of nicknames already in use
connection = sqlite3.connect("cgi-bin/lulan.db")
cursor = connection.cursor()
cursor.execute("SELECT nickname FROM user;")
usedNicks = []
for row in cursor.fetchall():
    usedNicks.append(row[0])
connection.close()

# Something wrong with input, return and modify input fields
if ("nickName" not in form) or (form["nickName"].value in usedNicks) or ("password1" not in form) or ("password2" not in form) or (form["password1"].value != form["password2"].value):
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
        sp = content.split('placeholder="Nickname ..."')
        content = 'placeholder="MISSING: Nickname."'.join(sp)
    # Fill in nickname if there is one/error when already used
    else:
        # nickname already used
        if form["nickName"].value in usedNicks:
            sp = content.split('placeholder="Nickname ..."')
            content = ('placeholder="NICK UNAVAILABLE: '+form["nickName"].value+'"').join(sp)
        # nickname is fine, fill it in
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
else:
    print("Content-Type: text/html\n")
    print("<!DOCTYPE html>")
    print("<p>")
    print("Benutzer wird angelegt: "+form["nickName"].value+"<br>\n")
    print("Passwort: "+form["password1"].value+"<br>\n")
    # These variables only get filled if there were values for them in the form
    firstName = ""
    lastName = ""
    if "firstName" in form:
        print("Vorname: "+form["firstName"].value+"<br>\n")
        firstName = form["firstName"].value
    else:
        print("Kein Vorname<br>\n")
    if "lastName" in form:
        print("Nachname: "+form["lastName"].value+"\n")
        lastName = form["lastName"].value
    else:
        print("Kein Nachname<br>\n")
    print("</p>")

    try:
        # Establish Database
        connection = sqlite3.connect("cgi-bin/lulan.db")

        # Connect to database and set the cursor
        cursor = connection.cursor()

        # Execute the user creation
        params = (firstName, lastName, form["nickName"].value, form["password1"].value)
        cursor.execute("INSERT INTO user (firstname, lastname, nickname, password) VALUES (?, ?, ?, ?);", params)

        # Close connection to database
        connection.commit()
        connection.close()
    except sqlite3.IntegrityError:
        print("<p>\nFehler! Benutzername ist bereits vergeben!\n</p>")
