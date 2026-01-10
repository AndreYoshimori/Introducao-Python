# Exercício 9.9: Crie um programa que receba uma lista de nomes de arquivos e os imprima, um por um.

from pathlib import Path


arquivos = ["capitulo4/ex_04.py", "capitulo6/ex_02.py", "capitulo8/ex_06.py"]

for arquivo in arquivos:
    caminho_entrada = Path(arquivo)
    with caminho_entrada.open("r", encoding="utf-8") as entrada:
        for linha in entrada:
            print(linha, end="")
        print()