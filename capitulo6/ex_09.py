# Exercício 6.9: Modifique o exemplo para pesquisar dois valores.
# Em vez de apenas p, leia outro valor v que também será procurado.
# Na impressão, indique qual dos dois valores foi achado primeiro.
L = [15, 7, 27, 39]

v1 = input('Digite o valor 1 a procurar: ')
while not v1.isnumeric():
    v1 = input('Por favor, insira apenas números. Digite o valor 1 a procurar: ')
v1 = int(v1)

v2 = input('Digite o valor 2 a procurar: ')
while not v2.isnumeric():
    v2 = input('Por favor, insira apenas números. Digite o valor 2 a procurar: ')
v2 = int(v2)

p1 = None
p2 = None
primeiro = None
i = 0
while i < len(L):
    if L[i] == v1:
        p1 = i + 1
        if primeiro is None:
            primeiro = v1
    elif L[i] == v2:
        p2 = i + 1
        if primeiro is None:
            primeiro = v2
    i += 1
if primeiro is None:
    print('Nenhum valor encontrado.')
else:
    print(f'{primeiro} foi encontrado primeiro.')
    if p1 is not None:
        print(f'{v1} foi encontrado na posição {p1}.')
    else:
        print(f'{v1} não foi encontrado.')
    if p2 is not None:
        print(f'{v2} foi encontrado na posição {p2}.')
    else:
        print(f'{v2} não foi encontrado.')