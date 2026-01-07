# Exercício 7.1: Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
# 1ª string: AABBEFAATT
# 2ª STRING: BE
# Resultado: BE encontrado na posição de AABBEFAATT

primeira = 'AABBEFAATT'
segunda = 'BE'

indice = primeira.find(segunda)

if indice >= 0:
    print(f'{segunda} encontrado no índice {indice} de {primeira}.')
else:
    print('Não encontrado.')
    