import _sqlite3
connection = sqlite3.connect("user.db")

cursor = connection.cursor()

sql_command = """
CREATE TABLE user (
userID INTEGER PRIMARY KEY,
FIRSTNAME VARCHAR(30),
LASTNAME VARCHAR(30),
NICKNAME VARCHAR(30),
GAMES VARCHAR(99999),
PASSWORD VARCHAR(30),
);"""
cursor.execute(sql_command)

sql.command = """INSERT INTO user
(FIRSTNAME, LASTNAME, NICKNAME, GAMES, PASSWORD)
VALUES ("""firstName""", """lastName""", """nickName""", """games""", """password1""");"""
cursor.execute(sql_command)

connection.commit()
connection.close()
