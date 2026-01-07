# Exercício 4: Escreva um programa que receba uma frase do usuário.
# Crie uma lista com todas as palavras da frase (separando por espaço).
# Depois, imprima as palavras em ordem inversa (última primeiro).

frase = input('Digite uma frase: ')
palavras = frase.split()

for i in range(len(palavras)):
    print(palavras[(len(palavras)) - 1 - i])
    