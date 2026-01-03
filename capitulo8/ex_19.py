# Exercício 8.19: Escreva um generator capaz de gerar a sequência dos números primos.

def gerador_primos(fim):
    num = 2
    while num <= fim:
        divisor = 2
        raiz_quadrada = num ** 0.5
        while divisor <= raiz_quadrada:
            if num % divisor == 0:
                break
            divisor += 1
        else:
            yield num
            
        num += 1

for primo in gerador_primos(100):
    print(primo)