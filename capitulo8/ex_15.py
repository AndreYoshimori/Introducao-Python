# Exercício 8.15: Altere o programa 7.2, o jogo da forca. Escolha a palavra a adivinhar utilizando números aleatórios.

import random


palavras = ["janela", "cadeira", "cachorro", "bicicleta", "telefone", "garrafa", "travesseiro", "montanha", "camiseta", "espelho"]

palavra = palavras[random.randint(0, len(palavras) - 1)]

for x in range(20):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""

    for letra in palavra:
        senha += letra if letra in acertos else "-"
        
    print(senha)

    if senha == palavra:
        print('\nVocê acertou')
        break

    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já tentou essa letra!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa            
        else:
            erros += 1
            print('Você errou')

    print('X==:==\nX  :  ')
    print('X  0  '  if erros >= 1 else "X")

    linha2 = ""
    if erros == 2:
        linha2 = '  |  '
    elif erros == 3:
        linha2 = ' \|  '
    elif erros >= 4:
        linha2 = ' \|/ '
    print(f'X{linha2}')
        
    linha3 = ""
    if erros == 5:
        linha3 += ' /   '
    elif erros >= 6:
        linha3  += ' / \ '
    print(f'X{linha3}')

    print('X\n==========')

    if erros == 6:
        print('\nEnforcado')
        print(f'A palavra era {palavra}')
        break