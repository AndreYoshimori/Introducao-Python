# Exercício 7.8: Escreva um programa para exibir todas as palavras de uma frase.
# Considere que uma palavra termina com um espaço em branco ou quando a string terminar. 
# Exemplo: "O rato roeu a roupa" deve imprimir 5.

frase = input('Digite uma frase para ver quantas palavras ela possui: ')
lista_palavras = frase.split()
quantidade_palavras = len(lista_palavras)

print(f'Essa frase possui {quantidade_palavras} palavras:')

for palavra in lista_palavras:
    print(palavra)