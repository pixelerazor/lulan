#!/usr/bin/python3

import os
import re
from printOperations import *
import cgi
import sqlite3

# Definitions that create the html page
def games():
    global y
    # Establish Database
    connection = sqlite3.connect("cgi-bin/lulan.db")

    # Connect to database and set the cursor
    cursor = connection.cursor()

    # Create table in database
    games = cursor.execute("SELECT * FROM games;")


    for uid, name in games:
        print("      <li>")
        print('         <label><input type="checkbox" name="'+name+'" value="'+str(uid)+'">'+name+'<label>')
        print("      </li>")
    # Close connection to database
    connection.commit()
    connection.close()

def gamesHtml():
    print("<div>")
    print("<form>")
    print("  <h3>Check the games you own:</h3>")
    print("  <h2>This will help us to find matching teammates respectively opponents.</h2>")
    print("  <fieldset>")
    print("    <ul>")
    games()
    print("    </ul>")
    print('    <p><button type="submit" class="button">Save</button></p>')
    print("  </fieldset>")
    print("</form>")
    print("</div>")

#Definitions that get the Data from the form in reg_games
def getFormData(y):
    form = cgi.FieldStorage()
    for i in y:
        searchterm = form.getvalue(y)
        print(searchterm)

# Get index file for editing
indent = printHeader()
_ = printNav(indent)
gamesHtml()
printFooter()
#getFormData(y)

#TODO: Solve the Problem with the missing file links
#TODO: Maybe add a "Add games" button
