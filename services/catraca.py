class Catraca:
    def __init__(self):
        pass

    def validar_ingresso(self, ingresso):
        if not ingresso.pago:
            return print("\033[31mAcesso negado: ingresso não pago.\033[0m")
        
        if ingresso.usado:
            return print("\033[31mAcesso negado: ingresso já utilizado.\033[0m")
        
        ingresso.usado = True
        return print("\033[32mAcesso liberado.\033[0m")
    