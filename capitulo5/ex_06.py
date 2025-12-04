# Exercício 5.6: Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada de multiplicação: 2x1 = 2, 2x2 = 4, ...

mult = input('Digite de qual número você deseja a tabuada: ')
while not mult.isnumeric():
    mult = input('Digite de qual número você deseja a tabuada: ')
mult = int(mult)

i = 1
while i <= 10:
    res = i * mult
    print(f'{i} x {mult} = {res}')
    i += 1