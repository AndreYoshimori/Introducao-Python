# Exercício 4.14: Reescreva o programa a seguir com if-elif-else. Adicione as linhas necessárias para fazê-lo funcionar em Python.

'''
if a < 10:
    print('a é menor que 10.')
if a >= 10 and a < 20:
    print('a é maior que 10 e menor que 20.')
if a >= 20:
    print('a é maior que 20;')
'''

a = 18

if a < 10:
    print('a é menor que 10.')
elif a >= 10 and a < 20:
    print('a é maior que 10 e menor que 20.')
else:
    print('a é maior que 20;')