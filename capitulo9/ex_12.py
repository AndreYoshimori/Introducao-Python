# Exercício 9.12: Modifique o programa do Exercício 9.11 para também registrar a linha e a coluna de cada ocorrência da palavra no arquivo.
# Para isso, utilize listas, nos valores de cada palavra, guardando a linha e a coluna de cada ocorrência.

import string
from pathlib import Path


caminho_entrada = Path("dados") / "texto.txt"

ocorrencias_palavras = {}

with caminho_entrada.open("r", encoding="utf-8") as entrada:
    n_linha = 1
    for linha in entrada:
        linha = linha.lower()

        i = 0
        while i < len(linha):
            while i < len(linha) and (linha[i] in string.punctuation or linha[i] == " "):
                i += 1

            if i >= len(linha):
                break

            coluna_inicio = i
            palavra = ""

            while i < len(linha) and not (linha[i] in string.punctuation or linha[i] == " "):
                palavra += linha[i]
                i += 1
            
            if palavra not in ocorrencias_palavras:
                ocorrencias_palavras[palavra] = []
            ocorrencias_palavras[palavra].append(f'Linha {n_linha} - Coluna {coluna_inicio}')

        n_linha += 1

print(ocorrencias_palavras)