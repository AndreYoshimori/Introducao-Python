# Exercício 10: Devido ao covid as cadeiras de cinema tem que ser utilizadas com um espaçamento de uma cadeira desocupada tanto na frente quanto atrás e dos lados. 
# Represente está situação com uma matriz 50x50 em que cada local (i,j) tem nele a palavra “vaga” ou ocupada.

def printa_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end = " ")
        print()


def cria_matriz():
    num_linhas = 50
    num_colunas = 50
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
                matriz[i][j] = 'ocup'
            else:
                matriz[i][j] = 'vaga'

matriz = cria_matriz()

tabuleiro_xadrez(matriz)
printa_matriz(matriz)
