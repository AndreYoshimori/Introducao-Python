# Exercício 3: Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da diagonal para 1.

def printa_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end = " ")
        print()


def diagonal_principal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

diagonal_principal(matriz)
printa_matriz(matriz)