#  SISTEMA DE CINEMA

## Filme
- titulo
- duracao
- classificacao

## Sala
- numero
- capacidade
- ocupada(0)

## Sessao
- filme
- horario
- sala
- ingressos_disponiveis

## Cliente
- ingresso
- nome
- comprar_ingresso()
- cancelar_ingresso()

## Ingresso
- sessao 
- poltrona
- valor
- pago
- pagar()
- cancelar()

## Cinema
- clientes
- filmes
- sessoes
- salas
- vender_ingresso()
- listar_sessoes()

## catraca
- validar_ingresso