# Exercício 8.16: Modifique o jogo do alienígena. 
# Crie uma variável que represente a vida do jogador, começando com 100.
# A partida termina quando você encontrar o alienígena ou quando a vida acabar (<=0).
# A cada erro, diminua a vida por um valor aleatório entre 5 e 20, representando um ataque do alienígena.
# Você pode retirar a parte do jogo que limita o número de tentativas e deixar apenas a vida do jogador ou do alienígena decidirem quando a partida termina.
# Exiba a vida do jogador antes de perguntar a próxima árvore.

import random


vida = 100

dano_min = 5
dano_max = 20

arvore = random.randint(1, 100)

print('Um alienígena está escondido atrás de uma árvore.')
print('Cada árvore foi numerada de 1 a 100.')
print(f'Você tem {vida} de vida, e a cada tentativa falha o alienígena te atacará, causando um dano aleatório entre {dano_min} e {dano_max}.')
print('Quando sua vida chegar a 0 ou menos, você morrerá.')
print('O alienígena se esconde.')

while vida > 0:
    while True:
        palpite = input(f'\nÁrvore: ')
        if palpite.isnumeric():
            palpite = int(palpite)
            if palpite >= 1 and palpite <= 100:
                break   
        print('Digite um número entre 1 e 100.')

    if palpite == arvore:
        print(f'\nVocê acertou!')
        break
    elif palpite > arvore:
        print('Muito alto')
    elif palpite < arvore:
        print('Muito baixo')

    dano = random.randint(dano_min, dano_max)
    print(f'O alienígena lhe causou {dano} de dano')

    vida -= dano
    print(f'Vida: {vida}')

else:
    print('\nO alienígena te derrotou.')
    print(f'Ele estava na árvore {arvore}')
    