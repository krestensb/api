import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS bilag (id INTEGER PRIMARY KEY, description text, price text, username text)"
cursor.execute(create_table)


connection.commit()
connection.close()