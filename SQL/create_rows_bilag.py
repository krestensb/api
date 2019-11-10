import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

insert_row = "INSERT INTO bilag VALUES (2,'2description','2price')"
cursor.execute(insert_row)

connection.commit()
connection.close()