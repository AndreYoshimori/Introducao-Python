# Exercício 9.4: Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando 
# e que gere um arquivo de saída com as linhas do primeiro seguidas das linhas do segundo arquivo.
# O nome do arquivo de saída também pode ser passado como parâmetro na linha de comando.

import sys 


arquivos = [sys.argv[1], sys.argv[2]]

nome_arquivo = "dados/juncao_arquivos.txt"

if len(sys.argv) >= 4:
    nome_arquivo = sys.argv[3]

with open(nome_arquivo, "w") as saida:
    for arquivo in arquivos:
        with open(arquivo, "r") as entrada:
            for linha in entrada:
                saida.write(linha)
            saida.write("\n")

        