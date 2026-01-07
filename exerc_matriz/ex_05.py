# Exercício 5: Faça uma função que recebe uma matriz quadrada e altera todos os elementos acima/abaixo da diagonal para 1.

def printa_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end = " ")
        print()


def altera_fora_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j:
                matriz[i][j] = 1

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

altera_fora_diagonal(matriz)
printa_matriz(matriz)
