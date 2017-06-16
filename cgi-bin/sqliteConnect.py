import sqlite3
#Establish Database
connection = sqlite3.connect("user.db")

#Connect to database and set the cursor
cursor = connection.cursor()

#Create table in database
sql_command = """
CREATE TABLE user (
userID INTEGER PRIMARY KEY,
FIRSTNAME VARCHAR(30),
LASTNAME VARCHAR(30),
NICKNAME VARCHAR(30),
GAMES VARCHAR(99999),
PASSWORD VARCHAR(30),
);"""

#Execute tablecreation
cursor.execute(sql_command)

#Add new user to table
sql.command = """INSERT INTO user
(FIRSTNAME, LASTNAME, NICKNAME, GAMES, PASSWORD)
VALUES ("""+form["firstName"].value+""", """+form["lastName"].value+""", """+form["nickName"].value+""", """+form["password1"].value+""");"""

#Execute the user creation
cursor.execute(sql_command)

#Close connection to database
connection.commit()
connection.close()
