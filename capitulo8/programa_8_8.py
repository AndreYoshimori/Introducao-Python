# Programa 8.8

def fibonacci(n):
    print(f'Calculando fibonacci {n}')
    if n <= 1:
        print(f'Fibonacci de {n} = {n}')
        return n
    else:
        print(f'Fibonacci de {n} = fibonacci {n-1} + fibonacci {n-2} = ...')
        resultado = fibonacci(n - 1) + fibonacci(n - 2)

        print(f'Fibonacci de {n} = fibonacci {n-1} + fibonacci {n-2} = {resultado}')
        return resultado
    
fibonacci(5)