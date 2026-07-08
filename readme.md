# ticket-system

Sistema desktop de compra de ingressos de cinema, desenvolvido em **Python** com **CustomTkinter**. Permite ao usuário navegar pelo catálogo de filmes, consultar sessões disponíveis (sala e horário) e escolher poltronas para finalizar a compra do ingresso.

---

## Sobre o projeto

O `ticket-system` simula o fluxo completo de compra de ingressos de um cinema, com interface gráfica própria (sem depender de navegador), organizado em camadas para manter o código limpo e de fácil manutenção.

---

## Funcionalidades

- **Catálogo de filmes** — listagem dos filmes disponíveis em cartaz
- **Sessões** — consulta de sala e horários disponíveis por filme
- **Seleção de poltronas** — mapa interativo de assentos (livre / selecionada / ocupada)
- **Cálculo automático do valor** — total atualizado conforme as poltronas escolhidas
- **Minha Conta** — tela de dados do usuário
- **Finalização da compra** — confirmação do ingresso

---

## Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — interface gráfica

---

## Estrutura do projeto

```
ticket-system/
│
├── main.py                    # ponto de entrada da aplicação
│
├── models/                    # entidades do sistema (dados)
│   ├── __init__.py
│   ├── filme.py
│   ├── sala.py
│   ├── sessao.py
│   ├── cliente.py
│   └── ingresso.py
│
├── services/                  # regras de negócio e lógica
│   ├── __init__.py
│   ├── catraca_service.py
│   └── cinema_service.py
│
├── ui/                        # telas e navegação (CustomTkinter)
│   ├── __init__.py
│   ├── app.py                 # controlador principal (troca de telas)
│   ├── tela_filmes.py         # catálogo de filmes
│   ├── tela_conta.py          # minha conta
│   └── tela_poltronas.py      # seleção de poltronas + valor
│
├── .gitignore
└── README.md
```