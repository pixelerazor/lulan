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

# Close connection to database
connection.commit()
connection.close()
