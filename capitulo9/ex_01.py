# Exercício 9.1: Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprimas todas as linhas desse arquivo.

import sys


with open(sys.argv[1], "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha, end="")
        