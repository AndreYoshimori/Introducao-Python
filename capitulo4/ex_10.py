# Exercício 4.10: Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da operação solicitada.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Qual operação você deseja realizar? soma(+), subtração(-), multiplicação(*), ou divisão(/) \n->')

res = None

if operacao == '+':
    res = num1 + num2
elif operacao == '-':
    res = num1 - num2
elif operacao == '*':
    res = num1 * num2
elif operacao == '/':
    if num1 != 0 and num2 != 0:
        res = num1 / num2
    else:
        print('Erro. Divisão por zero.')
else:
    print('Não conheço essa operação.')

if res is not None:
    print(res)