# Temos uma lista de números
numeros = [10, 15, 20, 25, 30]

# Use filter + lambda para manter apenas os números maiores que 20
# Resultado esperado:
# [25, 30]

maiores = list(filter(lambda x: x > 20, numeros))

print(maiores)