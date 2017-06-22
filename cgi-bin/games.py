#!/usr/bin/python3

import os
import re
from printOperations import *
import cgi
import sqlite3

# Definitions that create the html page
def games():
    # Establish Database
    connection = sqlite3.connect("cgi-bin/lulan.db")

    # Connect to database and set the cursor
    cursor = connection.cursor()

    # Create table in database
    games = cursor.execute("SELECT * FROM games;")

    listString = []
    for uid, name in games:
        listString.append("                <li>")
        listString.append('                    <label><input type="checkbox" name="'+str(uid)+'" value="'+name+'">'+name+'</label>')
        listString.append("                </li>")
    # Close connection to database
    connection.commit()
    connection.close()
    return '\n'.join(listString)

def gamesHtml():
    text = ("<div class='center'>",
            getFormData(),
            "    <h2>Check the games you own:</h2>",
            "    <h3>This will help us to find matching teammates and opponents.</h3>",
            "    <form action='games.py' method='post'>",
            "        <fieldset>",
            "            <ul>",
            games(),
            "            </ul>",
            '            <p><button type="submit" class="button">Save</button></p>',
            "        </fieldset>",
            "    </form>",
            "</div>\n"
           )
    print(indentNewlines('\n'.join(text), 3), end='')

#Definitions that get the Data from the form in reg_games
def getFormData():
    form = cgi.FieldStorage()
    text = []
    for i in form:
       text.append("<p>"+i+": "+form[i].value+"</p>")
    return '\n'.join(text)

# Get index file for editing
indent = printHeader()
_ = printNav(indent)
gamesHtml()
printFooter()

#TODO: Solve the Problem with the missing file links
#TODO: Maybe add a "Add games" button
