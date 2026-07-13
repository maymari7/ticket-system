import sqlite3


def carrega_tabela():
    conexao = sqlite3.connect("data/cinema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())
    conexao.close()


carrega_tabela()
