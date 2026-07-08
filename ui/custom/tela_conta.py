import customtkinter as ctk
from tela_filmes import filmes  # Supondo que 'filmes' seja a CLASSE da outra janela


def trocarTela(telaAtual, classeDestino):
    telaAtual.destroy()  # Fecha a janela atual com segurança
    nova_tela = classeDestino()  # Cria a instância da nova janela
    nova_tela.mainloop()  # Inicia o loop da nova janela


class MinhaConta(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x420")
        self.title("Minha Conta")
        self.configure(fg_color="#000000")

        # CORREÇÃO 1: Usamos lambda para adiar a execução da função
        # CORREÇÃO 2: Separamos o .pack() do botão para evitar bugs no Python
        self.botaoTroca = ctk.CTkButton(
            self, text="trocar a tela", command=lambda: trocarTela(self, filmes)
        )
        self.botaoTroca.pack(pady=50)


if __name__ == "__main__":
    conta = MinhaConta()
    conta.mainloop()
