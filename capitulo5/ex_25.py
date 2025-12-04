# Exercício 5.25: Escreva um programa que calcule a raiz quadrada de um número.
# Utilize o método de Newton para obter um resultado aproximado.
# Sendo n o número a obter a raiz quadrada, considere a base b=2.
# Calcule p usando a fórmula p=(b+(n/b))/2.
# Agora, calcule o quadrado de p.
# A cada passo, faça b=p e recalcule p usando a fórmula apresentada.
# Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

n = input('Digite o número que deseja saber a raiz quadrada: ')
while not n.isnumeric():
    n = input('Digite o número que deseja saber a raiz quadrada: ')
n = int(n)

b = 2
p = (b + (n/b)) / 2

while (n - p * p >= 0.0001) or (p * p - n >= 0.0001):
    b = p
    p = (b + (n/b)) / 2

print(f'A raiz quadrada de {n} é {p:.5f}')
