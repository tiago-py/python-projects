import sqlite3 as sql

con = sql.connect('usr.db')

c = con.cursor()
c.execute (''' CREATE TABLE IF NOT EXISTS teste(
        id INT PRIMARY KEY,
        nome TEXT not null,
        email TEXT not null,
        senha TEXT not null

)''')

con.commit()

