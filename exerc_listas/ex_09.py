# Exercício 9: Escreva um programa que leia uma lista de números e diga se ela está ordenada de forma crescente.
# Caso não esteja, diga a posição onde ocorre a primeira quebra da ordem.
import random
lista = [1, 4, 7, 8, 2]
print(lista)
i = 0
while i < (len(lista) - 1):
    if lista[i] < lista[i + 1]:
        i += 1
    else:
        print('Não está em ordem crescente.')
        print(f'A primeira quebra de ordem ocorre no índice {i} ({lista[i]})')
        break
else:
    print('Está em ordem crescente.')