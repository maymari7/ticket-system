from database import conectar
from models.filme import Filme


def inserir_filme(titulo, genero, duracao, classificacao, imagem):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO filmes(titulo, genero, duracao, classificacao, imagem) 
        VALUES(?, ?, ?, ?, ?)
        """,
        (titulo, genero, duracao, classificacao, imagem),
    )

    conexao.commit()
    conexao.close()


def listar_filmes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM filmes")
    linhas = cursor.fetchall()

    conexao.close()

    return [
        Filme(
            id=linha["id"],
            titulo=linha["titulo"],
            genero=linha["genero"],
            duracao=linha["duracao"],
            classificacao=linha["classificacao"],
            imagem=linha["imagem"],
        )
        for linha in linhas
    ]
