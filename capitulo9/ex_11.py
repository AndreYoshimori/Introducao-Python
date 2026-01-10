# Exercício 9.11: Crie um programa que leia um arquivo e crie um dicionário em que cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.

import string
from pathlib import Path


caminho_entrada = Path("dados") / "texto.txt"

contador_palavras = {}

with caminho_entrada.open("r", encoding="utf-8") as entrada:
    for linha in entrada:
        linha = linha.translate(str.maketrans("", "", string.punctuation))
        linha = linha.lower()
        palavras = linha.split()
        for palavra in palavras:
            if palavra not in contador_palavras:
                contador_palavras[palavra] = 0
            contador_palavras[palavra] += 1

print(contador_palavras)