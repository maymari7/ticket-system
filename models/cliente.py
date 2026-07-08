class Cliente:
    def __init__(self, nome, ingresso):
        self.nome = nome
        self.ingresso = ingresso

    def comprar_ingresso(self, ingresso):
        self.ingresso = ingresso

    def cancelar_ingresso(self):
        self.ingresso = None
