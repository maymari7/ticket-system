from services.filme_service import inserir_filme

filmes_teste = [
    ("Um novo amor", "romance", "2h05", "+16", "assets/img/HomemAranha.webp"),
    ("Missão Órion", "ficção", "2h20", "+16", "assets/img/MorteDemonio.webp"),
    ("Drama sem fim", "drama", "1h48", "+14", "assets/img/Obsessao.webp"),
    ("O Convite", "drama", "1h48", "+18", "assets/img/Oconvite.webp"),
    ("Toy Story", "animação", "1h35", "Livre", "assets/img/ToyStory.webp"),
]

for titulo, genero, duracao, classificacao, imagem in filmes_teste:
    inserir_filme(titulo, genero, duracao, classificacao, imagem)

print("Filmes inseridos com sucesso!!")
