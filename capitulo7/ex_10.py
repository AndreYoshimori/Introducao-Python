# Exercício 7.10: Modifique o Programa 7.2 de forma a utilizar uma lista de palavras. 
# No início pergunte um número e calcule o índice da palavra a utilizar pela fórmula: índice = (número * 776) % len(lista_de_palavras).

lista_palavras = ['banana', 'garrafa', 'copo', 'celular', 'comida', 'escola', 'sapato', 'geladeira', 'canoa', 'mesa' ]

numero = input('Digite um número inteiro qualquer para sortear uma palavra: ')
while not numero.isnumeric():
    numero = input('\nDigite um número inteiro qualquer: ')
numero = int(numero)

indice = (numero * 776) % len(lista_palavras)

palavra = lista_palavras[indice]

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
    