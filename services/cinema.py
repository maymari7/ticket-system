class Cinema:
    def __init__(self):
        self.clientes = []
        self.sessoes = []
        self.filmes = []
        self.salas = []

    def listar_sessoes(self):
        for sessao in self.sessoes:
            print(
                f"Filme: {sessao.filme.titulo}, "
                f"Sala: {sessao.sala.numero}, "
                f"Horário: {sessao.horario}, "
                f"Ingressos disponíveis: {sessao.ingresso_disponivel}"
            )

    def vender_ingresso(self, ingresso, cliente, sessao):
        cliente.comprar_ingresso(ingresso)
        sessao.ingresso_disponivel -= 1
        return ingresso
