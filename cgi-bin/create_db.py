import sqlite3

# Establish Database
connection = sqlite3.connect("user.db")

# Connect to database and set the cursor
cursor = connection.cursor()

# Create table in database
sql_command = """
CREATE TABLE user (
FIRSTNAME VARCHAR(30),
LASTNAME VARCHAR(30),
NICKNAME VARCHAR(30) PRIMARY KEY,
PASSWORD VARCHAR(30)
);"""

# Execute table creation
cursor.execute(sql_command)

# Close connection to database
connection.commit()
connection.close()

