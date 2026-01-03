# Exercício 8.18: Modifique o Progrma 8.26 para que receba dois parâmetros opcionais. 
# Um para indicar o caractere a imprimir antes do número, sendo o espaço em branco o valor padrão, caso este não seja passado.
# O segundo parâmetro opcional é quantos caracteres adicionar por nível, tendo 2 como valor padrão.

def imprime_lista(lista, nivel = 0, caractere = ' ', quantidade = 2):
    for elem in lista:
        if isinstance(elem, int):
            prefixo = caractere * (nivel * quantidade)
            print(f'{prefixo}{elem}')
        else:
            imprime_lista(elem, nivel + 1, caractere, quantidade)

lista = [1, [2, 3, 4], [5, 6, [7, 8, 9]], 10]

imprime_lista(lista, caractere='-', quantidade=3)