#!/usr/bin/python3

import os
import re
from printOperations import *
import cgi

# Create html page
def games():
    global y
    games = ["Act of Aggression", "Anno 1404", "Anno 1404: Venedig", "Anno 2205", "ARK: Survival Evolved", "Arma 2", "Arma 3", "Arma 3: Apex", "Battlefield 1", "Battlefield 2", "Battlefield 3", "Battlefield 4", "Battlefield 1", "Borderlands", "Borderlands 2", "Call of Duty 4: Modern Warfare", "Civilisation 5", "Civilisation 6", "Company of Heros 2", "Counter-Strike 1.6", "Counter-Strike Source", "Counter-Strike: Global Offensive", "Day of Defeat: Source", "DayZ", "Diablo 3", "Divinity: Original Sin", "Doom", "Dota 2", "Evolve", "Factorio", "Far Cry 3", "Far Cry 4", "Grand theft Auto V", "Half-Life 2", "Hearthstone", "Helldivers", "Left 4 Dead", "Left 4 Dead 2", "Overwatch", "Path of Exile", "Payday 2", "Portal 2", "Project Cars", "Rocket League", "Rust", "Star Citizen", "Star Wars: Battlefront", "Starcraft 2", "Team Fortress 2", "The Division", "The Elder Scrolls Online", "Total War: Attila", "Unreal Tournament 3", "War for the Overlord", "Wolfenstein: The new Order", "World of Warcraft"]
    x = [g.replace(' ', '') for g in games]
    y = [g.replace(':', '') for g in x]
    f = ['1', '2', '3', '4', '5']
    i = 0
    for a, b in zip(y, games):
        print('      <li>')
        print('         <label>')
        print('             <input type="checkbox" name="'+a+'" value="'+a+'" class="option">'+b+'</input>')
        print('             <select>')
        for a, b in zip(y, f):
            print('                 <option value="'+y[i]+'''_'''+b+'" class="select">Priorität '+b+'</option>')
        print('             </select>')
        print('         </label>')
        print('      </li>')
    return y

def gamesHtml():
    print("<form>")
    print("  <h2>Check the games you own and choose a priority:</h2>")
    print("  <fieldset>")
    print("    <ul>")
    games()
    print("    </ul>")
    print('    <p><button type="submit" class="button">Save</button></p>')
    print("  </fieldset>")
    print("</form>")

gamesHtml()