# Programa 9.37: Escreva um programa que leia o nome do aluno e quatro notas.
# No final, o programa deve gravar os dados lidos em um arquivos em disco, usando o formato JSON.

import json
from pathlib import Path


caminho_saida = Path("dados/turma.json")

turma = {}

while nome := input("\nNome do aluno: "):
    turma[nome] = []

    for i in range(4):
        nota = float(input(f"Nota {i+1}: "))
        turma[nome].append(nota)

with caminho_saida.open("w", encoding="utf-8") as saida:
    json.dump(turma, saida, indent=2, ensure_ascii=False)
