# Exercício 5.27: Escreva um programa que verifique se um número é palíndromo.
# Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
# Exemplo: 454, 10501
num = input('Digite um número para descobrir se é palíndromo: ')
if num == num[::-1]:
    print(f'{num} é palíndromo.')
else:
    print(f'{num} não é palíndromo.')