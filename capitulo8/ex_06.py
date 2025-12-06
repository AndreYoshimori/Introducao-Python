# Exercício 8.6: Reescreva o Programa 8.2 de forma a utilizar for em vez de while.

def soma(L):
    total = 0

    for i in range(len(L)):
        total += L[i]

    return total

L = [1, 7, 2, 9, 15]

print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4]))