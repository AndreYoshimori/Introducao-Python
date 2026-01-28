# Exercício 9.34: Altere o Programa 7.2, o jogo da forca. Dessa vez, utilize as funções de tempo para cronometrar a duração das partidas.

import time


inicio_do_jogo = time.time()

palavra = input('Digite a palavra secreta: ').lower().strip()

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
        break
    
fim_do_jogo = time.time()

duracao = fim_do_jogo - inicio_do_jogo

print(f"A duração da partida foi de {duracao:.0f} segundos.")