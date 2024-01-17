#!/usr/bin/env python3

"""Exibe relatorio de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades
"""

__version__ = "0.1.1"

salas = {
    "Sala 1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "Sala 2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}
atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

for nome_atividade, alunos_atividade in atividades.items():
    print(f"Atividade: {nome_atividade}")
    print("-" * 50)
    for nome_sala, alunos_sala in salas.items():
        alunos_sala_atividade = set(alunos_sala).intersection(alunos_atividade)
        print(f"Alunos da {nome_sala}: {alunos_sala_atividade}")
    print("-" * 50)
