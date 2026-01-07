# Exercício 9.12: Modifique o programa do Exercício 9.11 para também registrar a linha e a coluna de cada ocorrência da palavra no arquivo.
# Para isso, utilize listas, nos valores de cada palavra, guardando a linha e a coluna de cada ocorrência.

import string
from pathlib import Path

diretorio_entrada = Path("dados")
arquivo_entrada = "texto.txt"
caminho_entrada = diretorio_entrada / arquivo_entrada

contador_palavras = {}

with caminho_entrada.open("r", encoding="utf-8") as entrada:
    for linha in entrada:
        linha = linha.translate(str.maketrans("", "", string.punctuation))
        linha = linha.lower()
        palavras = linha.split()
        for palavra in palavras:
            if palavra not in contador_palavras:
                contador_palavras[palavra] = 0
            contador_palavras[palavra] += 1

print(contador_palavras)