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

class teamBuild:
    def __init__(self):
        self.team = []
        self.team.clear()

    def teamBuild2on2(self, player, i):
        a = player.pop()
        b = player.pop()
        self.team.insert(0, a)
        self.team.insert(0, b)
        self.team.insert(0, i) # Die Variable i steht für die ID bzw. die feststehende Nummer des Teams
        self.team.insert(3, 0)

    def outputTeam(self):
        print(self.team)

def fitPlayerCount(player):
    playerCount = len(player)
    if playerCount >= 8:
        while (math.log(playerCount, 2) % 1) != 0:
            random.shuffle(player)
            dropout = player.pop()
            print("Player: ", dropout, "was removed.")
            playerCount = len(player)
            print(playerCount)
    else:
        print("Players missing: " + str(8 - playerCount) + " Player")

def teamGroup():
    a = len(player)
    if (teamCount*2) > len(player):
        print("The Number of Teams is to high. There are not enough Player to built teams.")
    else:
        for i in range(teamCount):
            i += 1
            team = teamBuild()
            team.teamBuild2on2(player, i)
            team.outputTeam()

# Spieler werden aus der SQL-Datenbank in eine Liste importiert.
player = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]

# Anzahl an Teams angeben und ausgeben
fitPlayerCount(player)
teamCount = 12
teamGroup()

# ---- Ausstehende Aufgaben: -----

# 4. Anlegen zweier Klassen: Winnder- und Loserbrackets

# 5. Zuweisung der Werte 1 oder 0 zu den Teams

# 6. Sortieren der Teams in die Brackets

# 7. Randomisiertes aufeinandertreffen

# 8. Darstellung des Gewinners
