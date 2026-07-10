import customtkinter as ctk


class TelaFilmes(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x420")
        self.title("Minha Conta")
        self.configure(fg_color="#000000")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.top_frame = ctk.CTkFrame(self, height=35, fg_color="transparent")
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.top_frame.grid_columnconfigure(0, weight=0)
        self.top_frame.grid_columnconfigure((1, 2), weight=1)

        self.logo = ctk.CTkLabel(
            self.top_frame, text="IngressCine", font=("Arial", 26, "bold")
        )
        self.logo.grid(row=0, column=0, pady=10, padx=(20, 0), sticky="w")

        self.link_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.link_frame.grid(row=0, column=2, pady=10, padx=(0, 20), sticky="e")

        self.conta = ctk.CTkButton(
            self.link_frame,
            text="Minha Conta",
            font=("Arial", 12, "bold"),
            fg_color="transparent",
        )
        self.conta.grid(row=0, column=1)

        self.main_container = ctk.CTkFrame(self, fg_color="black")
        self.main_container.grid(row=1, column=0, sticky="nsew")

        self.main_container.grid_columnconfigure(0, weight=0)
        self.main_container.grid_columnconfigure(1, weight=1)
        self.main_container.grid_rowconfigure(0, weight=0)
        self.main_container.grid_rowconfigure(1, weight=0)

        self.titulo_catalogo = ctk.CTkLabel(
            self.main_container, text="Catálogo de Filmes", font=("Arial", 16, "bold")
        )
        self.titulo_catalogo.grid(row=0, column=0, pady=(40, 10), padx=(20, 0))

        self.catalogo_frame = ctk.CTkFrame(
            self.main_container, fg_color="transparent", height=100
        )
        self.catalogo_frame.grid(row=1, column=0, columnspan=2, padx=10, sticky="ew")

        self.catalogo_frame.columnconfigure((0, 1, 2), weight=1)

        # -------------- ADICIONANDO CATALOGOS
        filmes = [
            ("♥", "Um novo amor", "romance", "2h05"),
            ("🚀", "Missão Órion", "ficção", "2h20"),
            ("🎭", "Drama sem fim", "drama", "1h48"),
        ]

        for i, (icone, titulo, genero, duracao) in enumerate(filmes):
            card = self.criar_card(self.catalogo_frame, icone, titulo, genero, duracao)
            card.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

    def criar_card(self, pai, icone, titulo, genero, duracao):
        card = ctk.CTkFrame(
            pai,
            fg_color="#1f1f1f",
            corner_radius=12,
            border_width=1,
            border_color="#4c0505",
        )

        icone_label = ctk.CTkLabel(
            card, text=icone, font=("Arial", 32), text_color="#e63946"
        )
        icone_label.pack(pady=(20, 10))

        # Título
        titulo_label = ctk.CTkLabel(
            card, text=titulo, font=("Arial", 15, "bold"), text_color="white"
        )
        titulo_label.pack(pady=(0, 4), padx=15, anchor="w")

        # Gênero + duração
        info_label = ctk.CTkLabel(
            card, text=f"{genero} · {duracao}", font=("Arial", 12), text_color="#999999"
        )
        info_label.pack(pady=(0, 15), padx=15, anchor="w")

        return card


# --------------

filmes = TelaFilmes()
filmes.mainloop()
