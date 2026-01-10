# Exercício 9.10: Crie um programa que receba uma lista de nomes de arquivos e que gere apenas um grande arquivo de saída.

from pathlib import Path


arquivos_entrada = [("capitulo4/ex_04.py"), ("capitulo6/ex_02.py"), ("capitulo8/ex_06.py")]

caminho_saida = Path("dados") / "soma_arquivos.txt"

with caminho_saida.open("w") as saida:
    for arquivo in arquivos_entrada:
        caminho_entrada = Path(arquivo)
        with caminho_entrada.open("r") as entrada:
            for linha in entrada:
                saida.write(linha)
            saida.write("\n")