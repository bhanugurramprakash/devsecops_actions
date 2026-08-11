import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
user_input = input("Enter username: ")
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
