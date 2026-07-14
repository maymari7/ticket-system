from database import conectar


def vender_ingresso(sessao_id, assento):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO ingressos(sessao_id, assento) VALUES (?, ?)", (sessao_id, assento)
    )

    cursor.execute(
        """
        UPDATE sessoes 
        SET ingressos_disponiveis = ingressos_disponiveis - 1 
        WHERE id = ? """,
        (sessao_id,),  # virgulas para mostrar q é uma TUPLA
    )

    conexao.commit()
    conexao.close()
