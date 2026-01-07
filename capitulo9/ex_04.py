# Exercício 9.4: Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando 
# e que gere um arquivo de saída com as linhas do primeiro seguidas das linhas do segundo arquivo.
# O nome do arquivo de saída também pode ser passado como parâmetro na linha de comando.

import sys 


arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]

nome_arquivo = "soma_arquivos.txt"

if len(sys.argv) >= 4:
    nome_arquivo = sys.argv[3]

with open(arquivo1, "r") as entrada1, open(arquivo2, "r") as entrada2, open(nome_arquivo, "w") as saida:
    for linha in entrada1:
        saida.write(linha)
    for linha in entrada2:
        saida.write(linha)
        