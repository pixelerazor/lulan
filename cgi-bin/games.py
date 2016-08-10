#!/usr/bin/python3

import os
import re
from printOperations import *
import cgi

# Definitions that create the html page
def games():
    global y
    games = ["Act of Aggression", "Anno 1404", "Anno 1404: Venedig", "Anno 2205", "ARK: Survival Evolved", "Arma 2", "Arma 3", "Battlefield 1", "Battlefield 2", "Battlefield 3", "Battlefield 4", "Battlefield 1", "Borderlands", "Borderlands 2", "Call of Duty 4: Modern Warfare", "Civilisation 5", "Civilisation 6", "Company of Heros 2", "Counter-Strike 1.6", "Counter-Strike Source", "Counter-Strike: Global Offensive", "Day of Defeat: Source", "DayZ", "Diablo 3", "Divinity: Original Sin", "Doom", "Dota 2", "Evolve", "Factorio", "Far Cry 3", "Far Cry 4", "Grand theft Auto V", "Half-Life 2", "Hearthstone", "Helldivers", "Left 4 Dead", "Left 4 Dead 2", "Overwatch", "Path of Exile", "Payday 2", "Portal 2", "Project Cars", "Rust", "Star Citizen", "Star Wars: Battlefront", "Starcraft 2", "Team Fortress 2", "The Division", "The Elder Scrolls Online", "Total War: Attila", "Unreal Tournament 3", "War for the Overlord", "Wolfenstein: The new Order", "World of Warcraft"]
    x = [g.replace(' ', '') for g in games]
    y = [g.replace(':', '') for g in x]
    for a, b in zip(y, games):
        print("      <li>")
        print('         <label><input type="checkbox" name="'+a+'" value="'+a+'">"'+b+'"<label>')
        print("      </li>")
    return y

def gamesHtml():
    print("<form>")
    print("  <h3>Check the games you own:</h3>")
    print("  <h2>This will help us to find matching teammates respectively opponents.</h2>")
    print("  <fieldset>")
    print("    <ul>")
    games()
    print("    </ul>")
    print('    <p><button type="submit" class="button">Save</button></p>')
    print("  </fieldset>")

#Definitions that get the Data from the form in reg_games
def getFormData(y):
    form = cgi.FieldStorage()
    for i in y:
        searchterm = form.getvalue(y)
        print(searchterm)

# Get index file for editing
file = open("html/reg_games.html", "r")
content = file.read()
file.close()

#printHeader()
#printNav()
#gamesHtml()
#printFooter()
getFormData(y)

#TODO: Solve the Problem with the missing file links
#TODO: Maybe add a "Add games" button

