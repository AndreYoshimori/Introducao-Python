# Exercício 2: Crie uma lista com números de 1 a 20.
# Depois, remova todos os múltiplos de 3 dessa lista (sem usar outra lista).

numeros = list(range(1, 21))

i = 0
while i < len(numeros):
    if numeros[i] % 3 == 0:
        del numeros[i]
    else:
        i += 1

print(numeros)