# Exercício 9.1: Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprimas todas as linhas desse arquivo.

import sys
from pathlib import Path


caminho_entrada = Path(sys.argv[1])

with caminho_entrada.open("r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha, end="")
        