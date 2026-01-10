# Exercício 9.7: Crie um programa que leia um arquivo-texto e gere um arquivo de saída paginado.
# Cada linha não deve conter mais de 76 caracteres.
# Cada página terá no máximo 60 linhas.
# Adicione na última linha de cada página o número da página atual e o nome do arquivo original.

from pathlib import Path


diretorio = Path("dados")
arquivo_entrada = "livro.txt"
caminho_entrada = diretorio / arquivo_entrada
caminho_saida = diretorio / "livro_paginado.txt"

largura_linha = 76
linhas_por_pagina = 59

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
