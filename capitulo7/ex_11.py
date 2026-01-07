# Exercício 7.11: Modifique o Programa 7.2 para utilizar listas de strings para desenhar o boneco da forca.
# Você pode utilizar uma lista para cada linha e organizá-las em uma lista de listas.
# Em vez de controlar quando imprimir cada parte, desenhe nessas listas, substituindo o elemento a desenhar.

'''
Exemplo:
>>> linha = list("X------")
>>> linha
['x', '-', '-', '-', '-', '-', '-']
>>> linha[6] = "|"
>>> linha
['x', '-', '-', '-', '-', '-', '|']
>>> "".join(linha)
'X-----|'
'''

palavra = input('Digite a palavra secreta: ').lower().strip()

for x in range(20):
    print()

digitadas = []
acertos = []
erros = 0

linha1 = list('X==:==')
linha2 = list('X  :  ')
linha3 = list('X     ')
linha4 = list('X     ')
linha5 = list('X     ')
linha6 = list('X     ')
linha7 = list('==========')

desenho_forca = [linha1, linha2, linha3, linha4, linha5, linha6, linha7]

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

    if erros == 1:
        linha3[3] = '0'

    elif erros == 2:
        linha4[2] = "\\"

    elif erros == 3:
        linha4[3] = "|"

    elif erros == 4:
        linha4[4] = "/"

    elif erros == 5:
        linha5[2] = "/"

    elif erros == 6:
        linha5[4] = "\\"
    
    for i in range(len(desenho_forca)):
        linha = "".join(desenho_forca[i])
        print(linha)

    if erros == 6:
        print('\nEnforcado')
        print(f'A palavra era {palavra}')
        break
    