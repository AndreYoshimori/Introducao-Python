# Exercício 8.8: Usando a função mdc definida no exercício anterior, defina uma função para calcular o menor múltiplo comum (M.M.C) entre dois números.
# Em que |a x b| oide ser escrito em Python como: abs(a * b).

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
    
def mmc(a, b):
    return abs(a * b) // mdc(a, b)

num1 = 6
num2 = 8

print(f'O mínimo múltiplo comum entre {num1} e {num2} é {mmc(num1, num2)}')