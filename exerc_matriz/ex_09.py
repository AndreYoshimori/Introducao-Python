# Exercício 9: Faça um código que recebe uma matriz quadrada e retorna uma imagem com padrão de círculo.

import matplotlib.pyplot as plt


def cria_matriz():
    num_linhas = 233
    num_colunas = 233
    matriz = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    return matriz


def centro_circulo(matriz_quadrada):
    tamanho_matriz = len(matriz_quadrada)
    i_central = tamanho_matriz // 2
    raio = i_central // 2
    return i_central, raio


def cria_circulo(matriz):
    i_central, raio = centro_circulo(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            diferença_linha = abs(i - i_central)
            diferença_coluna = abs(j - i_central)
            if diferença_linha**2 + diferença_coluna**2 <= raio**2:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0

matriz = cria_matriz()
cria_circulo(matriz)

plt.imshow(matriz, cmap='gray')
plt.show()
