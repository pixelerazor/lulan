#!/usr/bin/python3

import os
import re
from printOperations import *
import cgi

#Definitions that get the Data from the form in reg_games
def getFormData(games):
    x = [g.replace(' ', '') for g in games]
    y = [g.replace(':', '') for g in x]
    form = cgi.FieldStorage()
    for i in y:
        searchterm = form.getvalue(i)
        print(searchterm)

games = ["Act of Aggression", "Anno 1404", "Anno 1404: Venedig", "Anno 2205", "ARK: Survival Evolved", "Arma 2", "Arma 3", "Arma 3: Apex", "Battlefield 1", "Battlefield 2", "Battlefield 3", "Battlefield 4", "Battlefield 1", "Borderlands", "Borderlands 2", "Call of Duty 4: Modern Warfare", "Civilisation 5", "Civilisation 6", "Company of Heros 2", "Counter-Strike 1.6", "Counter-Strike Source", "Counter-Strike: Global Offensive", "Day of Defeat: Source", "DayZ", "Diablo 3", "Divinity: Original Sin", "Doom", "Dota 2", "Evolve", "Factorio", "Far Cry 3", "Far Cry 4", "Grand theft Auto V", "Half-Life 2", "Hearthstone", "Helldivers", "Left 4 Dead", "Left 4 Dead 2", "Overwatch", "Path of Exile", "Payday 2", "Portal 2", "Project Cars", "Rocket League", "Rust", "Star Citizen", "Star Wars: Battlefront", "Starcraft 2", "Team Fortress 2", "The Division", "The Elder Scrolls Online", "Total War: Attila", "Unreal Tournament 3", "War for the Overlord", "Wolfenstein: The new Order", "World of Warcraft"]

# Get index file for editing
file = open("html/reg_games.html", "r")
content = file.read()
file.close()

#printHeader()
#printNav()
#gamesHtml()
#printFooter()
getFormData(games)# The list f contains the game priority

#TODO: Solve the Problem with the missing file links
#TODO: Maybe add a "Add games" button

