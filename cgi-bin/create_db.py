import sqlite3

# Establish Database
connection = sqlite3.connect("lulan.db")

# Connect to database and set the cursor
cursor = connection.cursor()

# Create table in database
sql_command = """
CREATE TABLE IF NOT EXISTS user (
    firstname VARCHAR(30),
    lastname VARCHAR(30),
    nickname VARCHAR(30) PRIMARY KEY,
    password VARCHAR(60)
);"""

# Execute table creation
cursor.execute(sql_command)

# Create table in database
sql_command = """
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    gamename VARCHAR(60)
);"""

# Execute table creation
cursor.execute(sql_command)

games = ["Act of Aggression", "Anno 1404", "Anno 1404: Venedig", "Anno 2205", "ARK: Survival Evolved", "Arma 2",
         "Arma 3", "Battlefield 1", "Battlefield 2", "Battlefield 3", "Battlefield 4", "Battlefield 1", "Borderlands",
         "Borderlands 2", "Call of Duty 4: Modern Warfare", "Civilisation 5", "Civilisation 6", "Company of Heros 2",
         "Counter-Strike 1.6", "Counter-Strike Source", "Counter-Strike: Global Offensive", "Day of Defeat: Source",
         "DayZ", "Diablo 3", "Divinity: Original Sin", "Doom", "Dota 2", "Evolve", "Factorio", "Far Cry 3", "Far Cry 4",
         "Grand theft Auto V", "Half-Life 2", "Hearthstone", "Helldivers", "Left 4 Dead", "Left 4 Dead 2", "Overwatch",
         "Path of Exile", "Payday 2", "Portal 2", "Project Cars", "Rust", "Star Citizen", "Star Wars: Battlefront",
         "Starcraft 2", "Team Fortress 2", "The Division", "The Elder Scrolls Online", "Total War: Attila",
         "Unreal Tournament 3", "War for the Overlord", "Wolfenstein: The new Order", "World of Warcraft"]

for game in games:
    cursor.execute("INSERT INTO games VALUES (NULL, ?);", (game,))

# Close connection to database
connection.commit()
connection.close()
