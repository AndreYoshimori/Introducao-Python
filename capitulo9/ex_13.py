# Exercício 9.13: Crie um programa que imprima as linhas de um arquivo.
# Esse programa deve receber três parâmetros pela linha de comando: o nome do arquivo, a linha inicial e a última linha a imprimir.

import sys
from pathlib import Path


caminho_entrada = Path(sys.argv[1])

inicio = int(sys.argv[2])
fim = int(sys.argv[3])

n_linha = 1

with caminho_entrada.open("r", encoding="utf-8") as entrada:
    for linha in entrada:
        if n_linha >= inicio:
            print(linha, end="")
        if n_linha == fim:
            break
        n_linha += 1
        