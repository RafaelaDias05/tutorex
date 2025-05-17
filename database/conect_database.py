import sqlite3

def conectar():
    return sqlite3.connect('tutorex.db')

def criar_tabelas():
    with open('database\\tutorex.sql', 'r') as f:
        script = f.read()
    conn = conectar()
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    conn.close()

criar_tabelas()