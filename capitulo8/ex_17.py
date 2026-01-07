# Exercício 8.17: Melhore o programa do exercício anterior perguntando ao jogador o nível de dificuldade desejado.
# No modo fácil, a vida começa com 100 e o alienígena pode causar entre 5, e 20 de dano, como anteriormente.
# No modo médio, a vida começa com 80 e o alienígena pode causar danos entre 10 e 25.
# Já no modo difícil, a vida começa com 75, e o alienígena causa danos entre 20 e 30.
# Adicione mensagens e caracteres para deixar o jogo mais divertido.

import random


print('Bem vindo ao jogo do alienígena!')

dificuldades = ['f', 'm', 'd']

while True:
    dificuldade = input('\nDeseja jogar na dificuldade fácil(f), médio(m), ou difícil(d): ').strip().lower()
    if dificuldade in dificuldades:
        break
    print('Digite f, m, ou d para prosseguir.')

valores = {'f': {'vida': 100,
                 'dano_min': 5,
                 'dano_max': 20},
            'm': {'vida': 80,
                 'dano_min': 10,
                 'dano_max': 25},
            'd': {'vida': 75,
                 'dano_min': 20,
                 'dano_max': 30}
            }

vida = valores[dificuldade]["vida"]

dano_min = valores[dificuldade]["dano_min"]
dano_max = valores[dificuldade]["dano_max"]

arvore = random.randint(1, 100)

print('\nUm alienígena está escondido atrás de uma árvore.')
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
    