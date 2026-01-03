# Temos uma lista de números
numeros = [1, 2, 3, 4]

# Use map + lambda para criar uma lista com o dobro de cada número
# Resultado esperado:
# [2, 4, 6, 8]

dobros = list(map(lambda x: x * 2, numeros))

print(dobros)