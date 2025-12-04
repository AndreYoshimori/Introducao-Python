# Exercício 8: Faça um programa que peça 5 números ao usuário e armazene em uma lista.
# Depois, ordene essa lista sem usar o método sort() nem sorted() — faça isso manualmente.

numeros = []

for i in range(5):
    num = input('Digite um número para adicionar à lista: ')
    while not num.isnumeric():
        num = input('Por favor, insira apenas números. Digite um número para adicionar à lista: ')
    num = int(num)
    numeros.append(num)

fim = len(numeros)

while fim > 1:
    trocou = False
    x = 0
    while x < fim - 1:
        if numeros[x] > numeros[x + 1]:
            trocou = True
            aux = numeros[x]
            numeros[x] = numeros[x + 1]
            numeros[x + 1] = aux
        x += 1
    if not trocou:
        break
    fim -= 1

print(numeros)