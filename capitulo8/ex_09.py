# Exercício 8.9: Rastreie o Programa 8.6 e compare o seu resultado com o apresentado.

def fatorial(n):
    print(f'Calculando o fatorial de {n}')
    if n == 0 or n == 1:
        print(f'Fatorial de {n} = 1')
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f'Fatorial de {n} = {fat}')       
        return fat

fatorial(4)