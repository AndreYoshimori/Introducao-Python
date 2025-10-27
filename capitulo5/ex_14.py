# Exercício 5.14: Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritimética.
contador = 0
soma = 0
while True:
    num = input('Digite um número ou 0 para finalizar: ')
    while not num.isnumeric():
        num = input('Digite um número oui 0 para finalizar: ')
    num = int(num)
    if num != 0:
        soma += num
        contador += 1
    else:
        break
if contador > 0:
    media = soma / contador
    print(f'Quantidade de números digitados: {contador}\nSoma dos números: {soma}\nMédia aritmética: {media:.2f}')
