# Exercício 4.3: Escreva um programa que leia três números e que imprima o maior e o menor.

num1 = 10
num2 = 5
num3 = 20

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior.')
if num2 > num1 and num2 > num3:
    print(f'{num2} é o maior.')
if num3 > num1 and num3 > num2:
    print(f'{num3} é o maior.')
if num1 < num2 and num1 < num3:
    print(f'{num1} é o menor.')
if num2 < num1 and num2 < num3:
    print(f'{num2} é o menor.')
if num3 < num1 and num3 < num2:
    print(f'{num2} é o menor.')