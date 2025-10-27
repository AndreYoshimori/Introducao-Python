# Exercício 5.8: Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado.
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
# Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4
primeiro = input('Digite o primeiro número para a multiplicação: ')
while not primeiro.isnumeric():
    primeiro = input('Digite o primeiro número para a multiplicação: ')
primeiro = int(primeiro)

segundo = input('Digite o segundo número para a multiplicação: ')
while not segundo.isnumeric():
    segundo = input('Digite o segundo número para a multiplicação: ')
segundo = int(segundo)

mult = 0
i = 0
while i < primeiro:
    mult += segundo
    i += 1
print(f'{primeiro} x {segundo} = {mult}')