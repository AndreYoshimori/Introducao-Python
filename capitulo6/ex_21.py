# Exercício 6.21: Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
# os valores comuns às duas listas
# os valores que só existem na primeira
# os valores que existem apenas na segunda
# uma lista com os elementos não repetidos das duas listas
# a primeira lista sem os elementos repetidos na segunda

a = [1, 3, 4, 6, 8, 10]
b = [2, 4, 5, 7, 8, 9]

print(set(a) & set(b))
print(set(a) - set(b))
print(set(b) - set(a))
print(set(a) ^ set(b))
print(set(a) - (set(a) & set(b)))