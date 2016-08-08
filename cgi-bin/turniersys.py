#!/usr/bin/python3
# Double-k.o Planung:
# Regeln/Bedingungen:
# 1. Turnier teilt sich von Beginn an in zwei Brackets. Winnerbracket und Loserbracket.
# 2. Nach der ersten Runde werden Gewinner und Verlierer in die entsprechenden Brackets aufgeteilt.
# 3. Winnerbracket wird nach der selben Methode weitergeführt.
# 4. Beginnerzahl mindestens eine Zweierpotenz.
# 5. Das Winnerbracket ist bis zum halbfinale identisch zum normalen K.O.-System.
# 6. Jede Runde des Loserbrackets wird in zwei Stufen gespielt.
#       a) In der ersten Stufe der ersten Runde treffen jeweils zwei Verlierer der ersten Runde des oberen Brackets aufeinander; in der ersten Stufe jeder folgenden Runde treffen jeweils zwei Gewinner der vorigen Runde aufeinander.
#       b) In der zweiten Stufe jeder Runde trifft stets ein Gewinner der ersten Stufe auf einen Verlierer derselben Runde aus dem oberen Bracket.
# 7. Am Ende des Turniers trifft der Gewinner der oberen Hälfte auf den Gewinner der unteren Hälfte.
# 8. Am Ende des Turniers trifft der Gewinner der oberen Hälfte auf den Gewinner der unteren Hälfte.
# Dieses Match wird vielfach als Finale gewertet. Ansonsten gilt folgende Regel: Gewinnt der Teilnehmer aus der oberen Hälfte, so ist das Turnier beendet.
# Gewinnt jedoch der Teilnehmer aus der unteren Hälfte, so haben beide einmal verloren und müssen ein zweites Mal gegeneinander spielen;
# dieses letztere Match entscheidet dann über die Plätze 1 und 2.

# Bei einem Spiel nach dem Double-k.-o. sind die Plätze drei und vier durch die Reihenfolge des Ausscheidens bestimmt; ein Spiel um den dritten Platz ist daher nicht erforderlich.
# Für n Mannschaften werden 2·(n-1) Spiele gespielt, bzw. eins mehr, falls das Finale wie oben beschrieben wiederholt wird.
# Beim einfachen K.-o.-System sind hingegen lediglich n-1 Spiele notwendig, also genau halbsoviele; bei einem Rundenturnier wären mindestens n·(n-1)/2 Spiele notwendig.

import random
import math
import sqlite3

# Unused as of now
class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# class for holding the team
class Team:
    # initialise the list
    def __init__(self):
        self.players = []

    # return player array as string when bare object name is called
    def __repr__(self):
        return str(self.players)

    # add a player to the team list. this is called by other classes creating teams to fill them.
    def addPlayer(self, player):
        self.players.append(player)

class TeamBuild:
    def __init__(self, players, teamSize):
        self.teams = []
        # Make sure player number is correct for team size
        while ((len(players) % teamSize) > 0):
            random.shuffle(players)
            dropout = players.pop()
            print("Too many players. Removed ", dropout, "<br>")
        # While there are players, create new teams
        while (len(players) > 0):
            newTeam = Team()
            # Add players to the current team
            for x in range(0, teamSize):
                random.shuffle(players)
                newMember = players.pop()
                newTeam.addPlayer(newMember)
            # Add the team
            self.teams.append(newTeam)

    def outputTeams(self):
        for team in self.teams:
            print(team, "<br>")

    def fitKoTeamCount(self, minTeams=4):
        teamCount = len(self.teams)
        if teamCount >= minTeams:
            while (math.log(teamCount, 2) % 1) != 0:
                random.shuffle(self.teams)
                dropout = self.teams.pop()
                print("Team: ", dropout, "was removed.<br>")
                teamCount = len(self.teams)
        else:
            print("Need at least: " + str(minTeams - teamCount))

# Spieler werden aus der SQL-Datenbank in eine Liste importiert.
players = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
           "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]

# Anzahl an Teams angeben und ausgeben
print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<h2>Team1 (5 players):</h2>")
team1 = TeamBuild(players, 5)
print("<h3>See teams:</h3>")
team1.outputTeams()
print("<h3>Switch to KO (minTeams=4):</h3>")
team1.fitKoTeamCount()
print("<h3>See teams:</h3>")
team1.outputTeams()

players = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
           "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]
print("<h2>Team2 (3 players):</h2>")
team2 = TeamBuild(players, 3)
print("<h3>See teams:</h3>")
team2.outputTeams()
print("<h3>Switch to KO (minTeams=8):</h3>")
team2.fitKoTeamCount(8)
print("<h3>See teams:</h3>")
team2.outputTeams()

# ---- Ausstehende Aufgaben: -----

# 4. Anlegen zweier Klassen: Winnder- und Loserbrackets

# 5. Zuweisung der Werte 1 oder 0 zu den Teams

# 6. Sortieren der Teams in die Brackets

# 7. Randomisiertes aufeinandertreffen

# 8. Darstellung des Gewinners
