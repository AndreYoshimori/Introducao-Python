# Exercício 8.7: Defina uma função recursiva que calcule o maior divisor comum (M.D.C) entre dois números a e b, em que a > b.

def mdc(a, b):
    if b == 0:
        return a
    else:
        resultado = mdc(b, a % b)
        return resultado

num1 = 30
num2 = 8

print(f'O máximo divisor comum entre {num1} e {num2} é {mdc(num1, num2)}')
