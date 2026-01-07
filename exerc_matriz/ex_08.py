# Exercício 8: Faça um código que transforma uma matriz quadrada 8x8 em um tabuleiro de xadrez.

import matplotlib.pyplot as plt


def cria_matriz():
    num_linhas = 8
    num_colunas = 8
    matriz = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    return matriz


def tabuleiro_xadrez(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = i + j
            if soma % 2 == 0:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1

matriz = cria_matriz()
tabuleiro_xadrez(matriz)

from matplotlib.colors import ListedColormap
cmap = ListedColormap(["#f5deb3", "#8b4513"])

plt.imshow(matriz, cmap=cmap)
plt.show()
