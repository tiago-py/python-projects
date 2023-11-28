import sqlite3 as sql

con = sql.connect('usr.db')

c = con.cursor()

def write(id, nome, email, senha):
        c.execute('''INSERT INTO teste(id, nome, email, senha) values(?,?,?,?)''', (id, nome, email, senha))
        con.commit()

def delete(x):
        c.execute('''DELETE FROM teste where nome=?''', x)
        con.commit()
def mostrarDados():
        c.execute('''SELECT * FROM teste''')
        con.commit()