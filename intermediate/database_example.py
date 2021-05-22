import sqlite3

connection = sqlite3.connect("../resources/dummy.db")

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PERSON
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL);
''')

# cursor.execute("INSERT INTO PERSON ('ID', 'NAME', 'AGE') VALUES ('1', 'John', 30), ('2', 'Max', 25);")
# connection.commit()

cursor.execute("SELECT * FROM PERSON")

rows = cursor.fetchall()

for row in rows:
   print(f"ID: {row[0]} Name: {row[1]} Age: {row[2]}")

connection.close()

