import sqlite3 as sql

con = sql.connect('usr.db')

c = con.cursor()
c.execute (''' CREATE TABLE IF NOT EXISTS teste(
        id INT PRIMARY KEY,
        nome TEXT not null,
        email TEXT not null,
        senha TEXT not null

)''')

def write(id, nome, email, senha):
        c.execute('''INSERT INTO teste(id, nome, email, senha) values(?,?,?,?)''', (id, nome, email, senha))
        con.commit()

def delete(x):
        c.execute('''SELECT nome FROM teste where nome=?''', x)
        con.commit()
