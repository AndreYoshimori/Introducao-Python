# Exercício 9.4: Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando 
# e que gere um arquivo de saída com as linhas do primeiro seguidas das linhas do segundo arquivo.
# O nome do arquivo de saída também pode ser passado como parâmetro na linha de comando.

import sys 
from pathlib import Path


arquivos_entrada = [sys.argv[1], sys.argv[2]]

caminho_saida = Path("dados") / "juncao_arquivos.txt"

if len(sys.argv) >= 4:
    caminho_saida = Path(sys.argv[3])

with caminho_saida.open("w") as saida:
    for arquivo in arquivos_entrada:
        caminho_entrada = Path(arquivo)
        with caminho_entrada.open("r") as entrada:
            for linha in entrada:
                saida.write(linha)
            saida.write("\n")
