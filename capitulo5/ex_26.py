# Exercício 5.26: Escreva um programa que calcule o resto da divisão inteira entre dois números.
# Utilize apenas as operações de soma e subtração para calcular o resultado.
n1 = input('Digite o dividendo: ')
while not n1.isnumeric():
    n1 = input('Digite o dividendo: ')
n1 = int(n1)
n1_inicial = n1

n2 = input('Digite o divisor: ')
while not n2.isnumeric():
    n2 = input('Digite o divisor: ')
n2 = int(n2)

while n1 >= n2:
    n1 -= n2
print(f'O resto da divisão de {n1_inicial} e {n2} é {n1}')