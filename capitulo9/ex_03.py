# Exercício 9.3: Crie um programa que leia os arquivos pares.txt e impares.txt e que crie um só arquivo paresimpares.txt 
# com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica.

from pathlib import Path


diretorio = Path("dados")
caminho_entrada1 = diretorio / "pares.txt"
caminho_entrada2 = diretorio / "impares.txt"
caminho_saida = diretorio / "paresimpares.txt"

with caminho_entrada1.open("r") as pares, caminho_entrada2.open("r") as impares, caminho_saida.open("w") as saida:
    for par, impar in zip(pares, impares):
        saida.write(par)
        saida.write(impar)
        