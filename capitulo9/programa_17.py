# Programa 9.17: Criando uma tabela de preços em formato JSON

import json
from pathlib import Path


tabela_de_precos = {}

print("Criador da tabela de preços")
print("Digite um nome de produto em branco para terminar")

while produto := input("Nome do produto:"):
    preco = input("Preço: ")
    tabela_de_precos[produto] = preco

with Path("dados/precos.json").open("w", encoding="utf-8") as arquivo:
    json.dump(tabela_de_precos, arquivo, indent=2, ensure_ascii=False)