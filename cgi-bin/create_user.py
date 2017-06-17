#!/usr/bin/python3

import os # Debug related
import cgi, sqlite3 # For getting form input
from printOperations import *

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
        sp = content.split("nickName ...")
        content = "MISSING: nickName".join(sp)
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
else:
    print("Content-Type: text/html\n")
    print("<!DOCTYPE html>")
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

# Establish Database
connection = sqlite3.connect("user.db")

# Connect to database and set the cursor
cursor = connection.cursor()

# Create table in database
sql_command = """
CREATE TABLE user (
userID INTEGER PRIMARY KEY,
FIRSTNAME VARCHAR(30),
LASTNAME VARCHAR(30),
NICKNAME VARCHAR(30),
GAMES VARCHAR(99999),
PASSWORD VARCHAR(30),
);"""

# Execute table creation
cursor.execute(sql_command)

# Add new user to table
sql.command = """INSERT INTO user
(FIRSTNAME, LASTNAME, NICKNAME, GAMES, PASSWORD)
VALUES ("""+form["firstName"].value+""", """+form["lastName"].value+""", """+form["nickName"].value+""", """+form["password1"].value+""");"""

# Execute the user creation
cursor.execute(sql_command)

# Close connection to database
connection.commit()
connection.close()



# Test: get information from database
connection = sqlite3.connect("user.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM user")
print("Komplette Tabelle ausgeben:")
result = cursor.fetchall()
for r in result:
    print(r)

