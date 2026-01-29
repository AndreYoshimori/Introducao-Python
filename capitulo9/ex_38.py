# Exercício 9.38: Modifique o programa anterior para que leia o mesmo arquivo, permitindo adicionar mais dados ao arquivo.
# Se o mesmo nome for digitado duas vezes, altere os dados para a nova entrada.

import json
from pathlib import Path


caminho = Path("dados/turma.json")

with caminho.open(encoding="utf-8") as entrada:
    turma = json.load(entrada)

while nome := input("\nNome do aluno: "):
    turma[nome] = []

    for i in range(4):
        nota = float(input(f"Nota {i+1}: "))
        turma[nome].append(nota)

with caminho.open("w", encoding="utf-8") as saida:
    json.dump(turma, saida, indent=2, ensure_ascii=False)
    