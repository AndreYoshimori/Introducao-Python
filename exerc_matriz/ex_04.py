# Exercício 4: Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da “contra-diagonal” para 1.

def printa_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end = " ")
        print()


def contra_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - i - 1] = 1

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

contra_diagonal(matriz)
printa_matriz(matriz)
