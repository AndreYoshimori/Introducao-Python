# Exercício 6: Faça uma função que recebe uma matriz quadrada e retorne sua transposta.

def printa_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end = " ")
        print()


def matriz_transposta(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:
                aux = matriz[i][j]
                matriz[i][j] = matriz[j][i]
                matriz[j][i] = aux

matriz = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

matriz_transposta(matriz)
printa_matriz(matriz)
