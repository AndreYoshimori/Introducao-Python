# Exercício 4.4: Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1250,0, calcule um aumento de 10%. Para o inferiores ou iguais, de 15%.

salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario * 0.10
    print(f'Você recebeu um aumento de 10%, ou seja, R$ {aumento:.2f}.')
if salario <= 1250:
    aumento = salario * 0.15
    print(f'Você recebeu um aumento de 15%, ou seja, R$ {aumento:.2f}.')
    