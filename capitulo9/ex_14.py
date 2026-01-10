# Exercício 9.14: Crie um programa que leia um arquivo-texto e elimine os espaços repetidos entre as palavras e no fim das linhas.
# O arquivo de saída também não deve ter mais de uma linha em branco repetida.

from pathlib import Path


diretorio = Path("dados")
caminho_entrada = diretorio / "texto_original.txt"
caminho_saida = diretorio / "texto_formatado.txt"

linhas_em_branco = 0

with caminho_entrada.open("r") as entrada, caminho_saida.open("w") as saida:
    for linha in entrada:
        linha = " ".join(linha.split())

        if linha == "":
            linhas_em_branco += 1
            if linhas_em_branco < 2:
                saida.write("\n")
            continue
        
        saida.write(f"{linha}\n")
        linhas_em_branco = 0
