import sqlite3

CAMINHO_BANCO = "data/cinema.db"


def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = (
        sqlite3.Row
    )  # acessa pelo nome da coluna: print(linha["titulo"]), não pela posição: print(linha[0])
    return conexao


def criar_banco():
    conexao = conectar()
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
