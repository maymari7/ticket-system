from models.cliente import Cliente
from models.filme import Filme
from models.sessao import Sessao
from models.ingresso import Ingresso
from services.cinema import Cinema
from models.sala import Sala
from database import criar_banco
import sqlite3

criar_banco()

cinema = Cinema()

cinema.filmes.extend(
    [Filme("Harry Potter", 120, "Livre"), Filme("Hermione Granger", 120, "Livre")]
)

cinema.salas.extend([Sala(1, 100), Sala(2, 50)])

cinema.sessoes.extend(
    [
        Sessao(cinema.filmes[0], cinema.salas[0], "18:00", 100),
        Sessao(cinema.filmes[1], cinema.salas[1], "20:00", 50),
    ]
)

cinema.clientes.extend([Cliente("João", None), Cliente("Maria", None)])

print("\033[1mSessões disponíveis:\033[0m")
cinema.listar_sessoes()

# Salas e sessões
sala1 = cinema.salas[0]
sessao1 = Sessao(cinema.filmes[0], sala1, "18:00", 100)

sala2 = cinema.salas[1]
sessao2 = Sessao(cinema.filmes[1], sala2, "20:00", 50)

# Venda de ingresso
cliente1 = cinema.clientes[0]
ingresso1 = Ingresso(sessao1, "A1", 20.0)

cinema.vender_ingresso(ingresso1, cliente1, sessao1)
cliente1.ingresso.pagar()  # Cliente paga o ingresso

print(cliente1.ingresso.exibir_detalhes())
