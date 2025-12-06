# Exercício 8.12: Escreva uma função que receba uma string e uma lista.
# A função deve comparar a string passada com os elementos da lista, também passada como parâmetro.
# Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.

def palavra_na_lista(palavra, lista):
    if palavra in lista:
        return True    
    return False

lista = ['banana', 'prato', 'escola', 'caderno']

palavra = input('Digite uma palavra: ').lower()

if palavra_na_lista(palavra, lista):
    print(f'{palavra} está na lista!')
else:
    print(f'{palavra} não está na lista.')