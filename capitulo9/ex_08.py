# Exercício 9.8: Modifique o programa do Exercício 9.7 para também receber o número de caracteres por linha e o número de linhas por página pela linha de comando.

from pathlib import Path
import sys


diretorio = Path("dados")
arquivo_entrada = "livro.txt"
arquivo_saida = "livro_paginado.txt"

caminho_entrada = diretorio / arquivo_entrada
caminho_saida = diretorio / arquivo_saida

largura_linha = int(sys.argv[1])
linhas_por_pagina = int(sys.argv[2]) - 1

with caminho_entrada.open("r") as entrada, caminho_saida.open("w") as saida:
    pagina = 1
    linhas_na_pagina = 0

    for linha in entrada:
        linha = linha.rstrip("\n")

        indice_atual = 0

        while indice_atual < len(linha) or (linha == "" and indice_atual == 0):
            nova_linha = linha[indice_atual:indice_atual + largura_linha]
            saida.write(f"{nova_linha}\n")

            indice_atual += largura_linha
            while indice_atual < len(linha) and linha[indice_atual] == " ":
                indice_atual += 1

            linhas_na_pagina += 1

            if linhas_na_pagina >= linhas_por_pagina:
                saida.write(f"Página {pagina} - {arquivo_entrada}\n\n")
                pagina += 1
                linhas_na_pagina = 0

    if linhas_na_pagina > 0:
        saida.write(f"Página {pagina} - {arquivo_entrada}\n\n")
