# Exercício 5.7: Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

mult = input('Digite de qual número você deseja a tabuada: ')
while not mult.isnumeric():
    mult = input('Digite de qual número você deseja a tabuada: ')
mult = int(mult)

inicio = input('Digite o número que vc deseja que ela comece: ')
while not inicio.isnumeric:
    inicio = input('Digite de qual número você deseja a tabuada: ')
inicio = int(inicio)

final = input('Digite o número que vc deseja que ela comece: ')
while not final.isnumeric:
    final = input('Digite de qual número você deseja a tabuada: ')
final = int(final)

while inicio <= final:
    res = inicio * mult
    print(f'{inicio} x {mult} = {res}')
    inicio += 1
    