# Exercício 3: Peça ao usuário 10 números e armazene em uma lista.
# Depois, crie uma nova lista só com os números que são maiores que a média dos 10 digitados.
numeros = []
soma = 0
for i in range(10):
    num = input('Digite um número: ')
    while not num.isnumeric():
        num = input('Por favor, insira apenas números. Digite um número: ')
    num = int(num)
    numeros.append(num)
    soma += num
media = soma / len(numeros)
maiores_media = []
for elem in numeros:
    if elem > media:
        maiores_media.append(elem)
print(f'Lista de números: {numeros}')
print(f'Média da lista: {media}')
print(f'Lista de números maiores que a média: {maiores_media}')