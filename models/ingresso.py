class Ingresso:
    def __init__(self, sessao, poltrona, valor, pago=False, usado=False):
        self.sessao = sessao
        self.poltrona = poltrona
        self.valor = valor
        self.pago = pago
        self.usado = usado

    def pagar(self):
        self.pago = True

    def cancelar(self):
        self.pago = False

    def exibir_detalhes(self):
        detalhes = (
            "\nDETALHES DO INGRESSO\n"
            f"{"-" * 40}\n"
            f"Filme: {self.sessao.filme.titulo}\n"
            f"Sala: {self.sessao.sala.numero}\n"
            f"Horário: {self.sessao.horario}\n"
            f"Poltrona: {self.poltrona}\n"
            f"Valor: R${self.valor:.2f}\n"
            f"{"-" * 40}\n"
        )
        return detalhes
