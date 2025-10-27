# Exercício 6.20: Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
# Exemplo = O rato -> {"O":1, "r":1, "a":1, "t":1, "o":1}
caracteres = {}
palavra = input('Digite uma palavra ou frase para ver a quantidade de cada letra: ')
for elem in palavra:
    if elem in caracteres:
        caracteres[elem] += 1
    elif elem == ' ':
        continue
    else:
        caracteres[elem] = 1
print(caracteres)