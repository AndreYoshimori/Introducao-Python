# Exercício 8.10: Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão.

def fibonacci(n):
    sequencia_fibonacci = []

    for i in range(n):
        if i <= 1:
            sequencia_fibonacci.append(1)
        else:
            proximo = sequencia_fibonacci[i - 1] + sequencia_fibonacci[i - 2]
            sequencia_fibonacci.append(proximo)
    
    return sequencia_fibonacci[n - 1]

num = 6

print(f'A posição {num} na sequência de fibonacci é {fibonacci(num)}')
