# Exercício 7: Uma matriz retangular da forma 5xN (5 linhas e N colunas) representa as notas de alunos em 5 provas.
# Cada linha é a nota de um aluno em uma das provas, enquanto cada coluna representa as 5 notas de um aluno somente.
# Cada nota deve ser ponderada pelo peso desta matéria, representada pelo vetor de pesos à esquerda. 
# Escreva um código que realiza esta operação e retorna uma lista com a média de cada aluno.

notas = [
    [7, 8, 6, 9, 5, 10, 4, 8, 7, 6],
    [5, 9, 7, 6, 8, 7, 6, 5, 9 ,8],
    [8, 6, 9, 7, 6, 5, 7, 9, 8, 7],
    [6, 7, 8, 5, 9, 8, 9, 6, 5, 9],
    [9, 5, 7, 8, 7, 6, 8, 7, 6, 8]
]

peso_materia = [1, 2, 3, 2, 1]

medias = []


def printa_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end = " ")
        print()


def pondera_notas(notas):
    for i in range(len(notas)):
        for j in range(len(notas[i])):
            notas[i][j] = notas[i][j] * peso_materia[i]


def tira_medias(notas_ponderadas):
    for coluna in range(len(notas_ponderadas[0])):
        media = 0
        
        for linha in range(len(notas_ponderadas)):
            media += notas_ponderadas[linha][coluna]

        media /= len(notas_ponderadas)
        medias.append(media)

print('Notas normais:')
printa_matriz(notas)

pondera_notas(notas)
print('\nNotas ponderadas:')
printa_matriz(notas)

tira_medias(notas)
print(f'\nMédias: {medias}')
