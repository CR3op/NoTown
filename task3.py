import sqlite3

with open('task1.py', 'r') as file:
    data = file.read()

parsed_data = data.split('\n')

con = sqlite3.connect('original_db.db')
cursor = con.cursor

for item in parsed_data:

    cursor.execute("INSERT INTO table (column_name) VALUES (?)", (item,))

con.commit()
con.close()