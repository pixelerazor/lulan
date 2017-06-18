import sqlite3

# Establish Database
connection = sqlite3.connect("lulan.db")

# Connect to database and set the cursor
cursor = connection.cursor()

# Create table in database
sql_command = """
CREATE TABLE user (
FIRSTNAME VARCHAR(30),
LASTNAME VARCHAR(30),
NICKNAME VARCHAR(30) PRIMARY KEY,
PASSWORD VARCHAR(60)
);"""

# Execute table creation
cursor.execute(sql_command)

# Create table in database
sql_command2 = """
CREATE TABLE games (
GAMEID VARCHAR(10) PRIMARY KEY,
GAMENAME VARCHAR(60),
);"""

# Execute table creation
cursor.execute(sql_command2)

# Close connection to database
connection.commit()
connection.close()

