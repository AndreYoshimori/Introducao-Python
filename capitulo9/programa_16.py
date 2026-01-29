# Programa 9.16: Abrindo um arquivo JSON e usando os dados

import json
from pathlib import Path


with Path("dados/lista.json").open(encoding="utf-8") as arquivo:
    turma = json.load(arquivo)

for aluno in turma:
    print("Nome:", aluno["nome"])
    print("Notas:", aluno["notas"])
    print("Média:", sum(aluno["notas"]) / len(aluno["notas"]))
    print()
    