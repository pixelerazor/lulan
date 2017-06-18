import sqlite3

# Establish Database
connection = sqlite3.connect("lulan.db")

# Connect to database and set the cursor
cursor = connection.cursor()

# Create table in database
sql_command = """
CREATE TABLE IF NOT EXISTS user (
FIRSTNAME VARCHAR(30),
LASTNAME VARCHAR(30),
NICKNAME VARCHAR(30) PRIMARY KEY,
PASSWORD VARCHAR(60)
);"""

# Execute table creation
cursor.execute(sql_command)

# Create table in database
sql_command2 = """
CREATE TABLE IF NOT EXISTS games (
GAMEID UNSIGNED INT(10) PRIMARY KEY,
GAMENAME VARCHAR(60)
);"""

# Execute table creation
cursor.execute(sql_command2)

# Close connection to database
connection.commit()
connection.close()

