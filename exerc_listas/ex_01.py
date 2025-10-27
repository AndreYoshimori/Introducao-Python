# Exercício 1: Peça ao usuário para digitar vários números inteiros (um por vez).
# Quando ele digitar 0, pare de pedir números.
# Armazene todos os números em uma lista e depois:
# - Imprima a média dos números
# - Imprima o maior e o menor valor
numeros = []
while True:
    num = input('Digite um número inteiro ou 0 para finalizar: ')
    while not num.isnumeric():
        num = input('Por favor, insira apenas números. Digite um número inteiro ou 0 para finalizar: ')
    num = int(num)
    if num == 0:
        break
    numeros.append(num)
soma = 0
maior = numeros[0]
menor = numeros[0]
for elem in numeros:
    soma += elem
    if maior < elem:
        maior = elem
    elif menor > elem:
        menor = elem
media = soma / len(numeros)
print(f'Média: {media}')
print(f'Maior valor da lista: {maior}')
print(f'Menor valor da lista: {menor}')