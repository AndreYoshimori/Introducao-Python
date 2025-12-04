# Exercício 5.22: Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

while True:
    opcao = input('Digite o número da operação da tabuada ou 0 para sair: 1 - Adição / 2 - Subtração / 3 - Divisão / 4 - Multiplicação\n->')
    while opcao != '0' and opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
        opcao = input('Digite o número da operação da tabuada ou 0 para sair: 1 - Adição / 2 - Subtração / 3 - Divisão / 4 - Multiplicação\n->')

    if opcao == '0':
        break
    
    num = input('Digite o número escolhido para a tabuada: ')
    while not num.isnumeric():
        num = input('Digite o número escolhido para a tabuada: ')
    num = int(num)

    i = 1
    while i <= 10:
        if opcao == '1':
            print(f'{num} + {i} = {num + i}')
            i += 1
        elif opcao == '2':
            print(f'{num} - {i} = {num - i}')
            i += 1
        elif opcao == '3':
            print(f'{num} / {i} = {num / i}')
            i += 1
        elif opcao == '4':
            print(f'{num} x {i} = {num * i}')
            i += 1
    print('')