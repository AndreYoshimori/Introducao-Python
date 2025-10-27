# Exercício 5.9: Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo.
# Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
dividendo = input('Digite o dividendo: ')
while not dividendo.isnumeric():
    dividendo = input('Digite o dividendo: ')
dividendo = int(dividendo)

divisor = input('Digite o divisor: ')
while not divisor.isnumeric():
    divisor = input('Digite o divisor: ')
divisor = int(divisor)

dividendo_original = dividendo
divisao = 0
while dividendo >= divisor:
    dividendo -= divisor
    divisao += 1
print(f'{dividendo_original} / {divisor} = {divisao}\nResto: {dividendo}')