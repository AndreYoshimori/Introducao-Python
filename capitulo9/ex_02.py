# Exercício 9.2: Modifique o programa do exercício 9.1 para que receba mais dois parâmetros: a linha de início e a de fim da impressão.
# O programa deve imprimir apenas as linhas entre esses dois valores (incluindo as linhas de início e fim).

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
        