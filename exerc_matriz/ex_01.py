# Exercício 1: Faça uma função que printa uma matriz da maneira convencional, ou seja, uma linha abaixo da outra. 

'''def printa_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print()'''


def printa_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end = " ")           
        print()

matriz = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
    ]

printa_matriz(matriz)
