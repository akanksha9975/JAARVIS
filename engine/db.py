import csv
# used to create database
import sqlite3   

con = sqlite3.connect("jarvis.db")

cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


# query = "INSERT INTO sys_command VALUES (null,'oneNote', 'C:\\Program Files\\Microsoft Office\\root\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# con.commit()




# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)


# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()
# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/')"
# cursor.execute(query)
# con.commit()

# testing module
# app_name = "oneNote"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])
