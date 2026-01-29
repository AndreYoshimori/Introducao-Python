# Programa 9.15: Lendo um arquivo JSON

import json
from pathlib import Path


with Path("dados/dados.json").open() as arquivo:
    dados = json.load(arquivo)

print(dados["nome"])
print(dados["valores"])
