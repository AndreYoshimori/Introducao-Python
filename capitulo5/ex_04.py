# Exercício 5.4: Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

fim = input('Digite o último número da lista: ')
while not fim.isnumeric():
    fim = input('Digite o último número da lista: ')
fim = int(fim)

x = 0
print(f'De {x} a {fim}, os números ímpares são: ')
while x <= fim:
    if x % 2 != 0:
        print(x)
    x += 1