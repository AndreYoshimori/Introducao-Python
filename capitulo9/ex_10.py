# Exercício 9.10: Crie um programa que receba uma lista de nomes de arquivos e que gere apenas um grande arquivo de saída.

from pathlib import Path


arquivos = [Path("capitulo4/ex_04.py"), Path("capitulo6/ex_02.py"), Path("capitulo8/ex_06.py")]

diretorio_saida = Path("dados")
arquivo_saida = "soma_arquivos.txt"
caminho_saida = diretorio_saida / arquivo_saida

with caminho_saida.open("w") as saida:
    for arquivo in arquivos:
        with arquivo.open("r") as entrada:
            for linha in entrada:
                saida.write(linha)
            saida.write("\n")