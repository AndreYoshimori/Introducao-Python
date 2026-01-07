# Exercício 6.22: Escreva um programa que compare duas listas.
# Considere a primeira lista como a versão inicial e a segunda como a versão após alterações.
# Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
# os elementos que não mudaram
# os novos elementos
# os elementos que foram removidos

inicial = [1, 3, 4, 6, 8, 10]
nova = [2, 4, 5, 7, 8, 9]

print(f'Elementos que não mudaram: {set(inicial) & set(nova)}')
print(f'Novos elementos: {set(nova) - set(inicial)}')
print(f'Elementos removidos: {set(inicial) - set(nova)}')
