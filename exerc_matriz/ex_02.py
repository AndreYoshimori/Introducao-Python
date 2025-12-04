# Exercício 2: Faça uma função que recebe de parâmetros as dimensões (linhas e colunas) e retorna uma matriz preenchida de zeros com essas dimensões.

def printa_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end = " ")
        print()


def valida_int(msg):
    entrada = input(msg)
    while not entrada.isnumeric():
        entrada = input(msg)
    entrada = int(entrada)
    return entrada


def cria_matriz():
    num_linhas = valida_int('Digite o número de linhas da matriz: ')
    num_colunas = valida_int('Digite o número de colunas da matriz: ')
    matriz = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    return matriz

matriz = cria_matriz()

printa_matriz(matriz)