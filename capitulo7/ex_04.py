# Exercício 7.4: Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
# String: TTAAC
# T: 2x
# A: 2x
# c: 1x

palavra = 'TTAAC'

contagem_caractere = {}

for caractere in palavra:
    if caractere not in contagem_caractere:
        contagem_caractere[caractere] = 0
    contagem_caractere[caractere] += 1

for chave, valor in contagem_caractere.items():
    print(f'{chave}: {valor}x')
    