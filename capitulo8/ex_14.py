# Exercício 8.14: Altere o Programa 8.22 de forma que o usuário tenha três chances de acertar o número. 
# O programa termina se o usuário acertar ou errar três vezes.

import random


i = 0
while i < 3:
    n = random.randint(1, 10)

    while i < 3:
        x = input('\nEscolha um número entre 1 e 10: ')
        while not x.isnumeric():
            print('\nDigite um número!')
            x = input('\nEscolha um número entre 1 e 10: ')
        x = int(x)

        i += 1

        if x == n:
            print('\nVocê acertou!')
            if i < 3:
                print('\nDecidindo outro número aleatório...')
            break
        else:
            print('\nVocê errou.')