# Exercício 5.5: Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

fim = input('Digite o último número da lista: ')
while not fim.isnumeric():
    fim = input('Digite o último número da lista: ')
fim = int(fim)

x = 0

print(f'De {x} a {fim}, os números múltiplos de 3 são: ')

while x <= fim:
    print(x)
    x += 3