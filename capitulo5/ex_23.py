# Exercício 5.23: Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

num = input('Digite um número para verificar se é ou não um número primo: ')
while not num.isnumeric():
    num = input('Digite um número para verificar se é ou não um número primo: ')
num = int(num)

if num < 2:
    print('Não é primo')
elif num == 2:
    print(f'{num} é um número primo.')
elif num % 2 == 0:
    print(f'{num} não é primo.')
else:
    primo = True
    i = 3
    while i < num:
        if num % i == 0:
            primo = False
            break
        i += 2
    if primo:
        print(f'{num} é primo.')
    else:
        print(f'{num} não é primo.')