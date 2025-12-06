# Exercício 8.1: Escreva uma função que retorne o maior de dois números.
# Valores esperados:
# máximo(5, 6) == 6
# máximo(2, 1) == 2
# máximo(7, 7) == 7

def maior_valor(numero1, numero2):
    if numero1 > numero2:
        return numero1
    return numero2

num1 = 5
num2 = 6

print(f'O maior valor entre {num1} e {num2} é {maior_valor(num1, num2)}')