# Exercício 3.10: Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário em porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.
salario = float(input('Digite seu salário atual: '))
porcentagem = float(input('Digite a porcentagem do seu aumento: '))
aumento = porcentagem / 100 * salario
novo_salario = salario + aumento
print(f'O aumento é de R$ {aumento}.')
print(f'O novo salário é R$ {novo_salario}.')