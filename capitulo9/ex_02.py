# Exercício 9.2: Modifique o programa do exercício 9.1 para que receba mais dois parâmetros: a linha de início e a de fim da impressão.
# O programa deve imprimir apenas as linhas entre esses dois valores (incluindo as linhas de início e fim).

import sys


inicio = sys.argv[2]
inicio = int(inicio)

fim = sys.argv[3]
fim = int(fim)

numero_linha = 1

with open(sys.argv[1], "r") as arquivo:
    for linha in arquivo:
        if numero_linha >= inicio:
            print(linha, end="")
        if numero_linha == fim:
            break
        numero_linha += 1
        