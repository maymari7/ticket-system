import sqlite3


def criar_banco():
    conexao = sqlite3.connect("data/cinema.db")
    cursor = conexao.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    genero TEXT,
                    duracao TEXT,
                    imagem TEXT
                )
                """)

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS salas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero INTEGER NOT NULL,
                    capacidade INTEGER NOT NULL
                )
                """)

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS sessoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filme_id INTEGER NOT NULL,
                    sala_id INTEGER NOT NULL,
                    horario TEXT NOT NULL,
                    ingressos_disponiveis INTEGER NOT NULL,
                    FOREIGN KEY (filme_id) REFERENCES filmes (id),
                    FOREIGN KEY (sala_id) REFERENCES salas (id)
                )
                """)

    conexao.commit()
    conexao.close()


def carrega_tabela():
    conexao = sqlite3.connect("data/cinema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())
    conexao.close()


carrega_tabela()
