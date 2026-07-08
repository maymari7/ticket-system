import customtkinter as ctk


class TelaFilmes(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x420")
        self.title("Minha Conta")
        self.configure(fg_color="#FFFFFF")

        self.botaoTroca = ctk.CTkButton(self, text="trocar a tela").pack()


filmes = TelaFilmes()
if __name__ == "__main__":
    filmes.mainloop()
