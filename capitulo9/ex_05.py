# Exercício 9.5: Crie um programa que inverta a ordem das linhas do arquivo pares.txt.
# A primeira linha deve conter o maior número; e a última, o menor.

from pathlib import Path


caminho_arquivo = Path("dados") / "pares.txt"

with caminho_arquivo.open("r") as entrada:
    lista_linhas = entrada.readlines()

total_linhas = len(lista_linhas)
i = total_linhas - 1

with caminho_arquivo.open("w") as saida:
    while i >= 0:
        saida.write(lista_linhas[i])
        i -= 1
        