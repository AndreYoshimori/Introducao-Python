# Temos uma lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Primeiro:
# - mantenha apenas os números pares
# Depois:
# - dobre esses números

# Resultado esperado:
# [4, 8, 12]

resultado = list(
    map(
        lambda x: x * 2, 
        filter(lambda x: x % 2 == 0, numeros)
        )
)

print(resultado)
