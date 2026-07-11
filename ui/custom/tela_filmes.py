import customtkinter as ctk
from PIL import Image


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
            hover_color="#4c0505",
        )
        self.conta.grid(row=0, column=1)

        self.main_container = ctk.CTkScrollableFrame(self, fg_color="black")
        self.main_container.grid(row=1, column=0, sticky="nsew")

        self.main_container.grid_columnconfigure(0, weight=0)
        self.main_container.grid_columnconfigure(1, weight=1)

        #  -------------- CARTAZES
        self.titulo_catalogo = ctk.CTkLabel(
            self.main_container,
            text="Em Cartaz",
            font=("Arial", 16, "bold"),
        )
        self.titulo_catalogo.grid(
            row=0, column=0, pady=(40, 10), padx=(20, 0), sticky="w"
        )

        self.catalogo_frame = ctk.CTkScrollableFrame(
            self.main_container,
            fg_color="transparent",
            height=300,
            orientation="horizontal",
        )
        self.catalogo_frame.grid(row=1, column=0, columnspan=2, padx=10, sticky="ew")

        filmes = [
            ("assets/img/HomemAranha.webp", "Um novo amor", "romance", "2h05"),
            ("assets/img/MorteDemonio.webp", "Missão Órion", "ficção", "2h20"),
            ("assets/img/Obsessao.webp", "Drama sem fim", "drama", "1h48"),
            ("assets/img/Oconvite.webp", "Drama sem fim", "drama", "1h48"),
            ("assets/img/ToyStory.webp", "Drama sem fim", "drama", "1h48"),
            ("assets/img/HomemAranha.webp", "Um novo amor", "romance", "2h05"),
            ("assets/img/MorteDemonio.webp", "Missão Órion", "ficção", "2h20"),
            ("assets/img/Obsessao.webp", "Drama sem fim", "drama", "1h48"),
            ("assets/img/Oconvite.webp", "Drama sem fim", "drama", "1h48"),
            ("assets/img/ToyStory.webp", "Drama sem fim", "drama", "1h48"),
        ]

        for i, (image, titulo, genero, duracao) in enumerate(filmes):
            foto_img = ctk.CTkImage(
                light_image=Image.open(image),
                dark_image=Image.open(image),
                size=(150, 200),
            )
            card = self.criar_card(
                self.catalogo_frame, foto_img, titulo, genero, duracao
            )
            card.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

        # -------------- SESSOES
        self.titulo_sessoes = ctk.CTkLabel(
            self.main_container,
            text="Próximas Sessões",
            font=("Arial", 16, "bold"),
        )
        self.titulo_sessoes.grid(
            row=2, column=0, pady=(40, 10), padx=(20, 0), sticky="w"
        )
        self.sessoes_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.sessoes_frame.grid(row=3, column=0, columnspan=2, padx=10, sticky="ew")

        self.sessoes_frame.columnconfigure(0, weight=1)

        sessao = [
            ("Um novo amor", "sala 4", "12h00", "35 ingressos disponiveis"),
            ("Um novo amor", "sala 5", "16h50", "50 ingressos disponiveis"),
        ]
        for s, (filme, sala, horário, ingresso_disponivel) in enumerate(sessao):
            sessao_disponivel = self.gerar_sessao(
                self.sessoes_frame, filme, sala, horário, ingresso_disponivel
            )
            sessao_disponivel.grid(row=s, column=0, padx=10, pady=10, sticky="ew")

            sessao_disponivel.columnconfigure(0, weight=0)
            sessao_disponivel.columnconfigure(1, weight=1)
        # --------------  CRIAR CARTAZ --------------

    def criar_card(self, pai, foto_img, titulo, genero, duracao):
        card = ctk.CTkFrame(
            pai,
            fg_color="#1f1f1f",
            corner_radius=12,
            border_width=1,
            border_color="#4c0505",
            width=200,
            height=280,
        )
        card.pack_propagate(False)

        # foto moldura
        foto_frame = ctk.CTkFrame(card, fg_color="orange", height=100, width=180)
        foto_frame.pack(pady=10)

        foto_label = ctk.CTkLabel(foto_frame, image=foto_img, text="")
        foto_label.pack()

        # Título
        titulo_label = ctk.CTkLabel(
            card, text=titulo, font=("Arial", 15, "bold"), text_color="white"
        )
        titulo_label.pack(pady=(0, 4), padx=15, anchor="w")

        info_label = ctk.CTkLabel(
            card, text=f"{genero} · {duracao}", font=("Arial", 12), text_color="#999999"
        )
        info_label.pack(pady=(0, 15), padx=15, anchor="w")

        return card

        # -------------- GERAR SESSOES --------------

    def gerar_sessao(self, pai, filme, sala, horario, ingresso_disponivel):
        sessao_disponivel = ctk.CTkFrame(
            pai,
            fg_color="#1f1f1f",
            corner_radius=12,
            border_width=1,
            border_color="#4c0505",
        )

        filme_label = ctk.CTkLabel(
            sessao_disponivel,
            text=filme,
            font=("Arial", 15, "bold"),
            text_color="white",
        )
        filme_label.grid(row=0, column=0, pady=(10, 2), padx=(10, 0), sticky="w")

        sala_label = ctk.CTkLabel(
            sessao_disponivel, text=sala, font=("Arial", 15, "bold"), text_color="white"
        )
        sala_label.grid(row=1, column=0, pady=2, padx=(10, 0), sticky="w")

        horario_label = ctk.CTkLabel(
            sessao_disponivel,
            text=horario,
            font=("Arial", 15, "bold"),
            text_color="white",
        )
        horario_label.grid(row=2, column=0, pady=2, padx=(10, 0), sticky="w")

        ingresso_disponivel_label = ctk.CTkLabel(
            sessao_disponivel,
            text=ingresso_disponivel,
            font=("Arial", 15, "bold"),
            text_color="red",
        )
        ingresso_disponivel_label.grid(
            row=1, column=1, pady=2, padx=(0, 10), sticky="e"
        )

        return sessao_disponivel


filmes = TelaFilmes()
filmes.mainloop()
