# Temos uma lista de produtos
# Cada produto é uma tupla (nome, preco)

produtos = [
    ("Teclado", 120),
    ("Mouse", 80),
    ("Monitor", 900),
    ("Cabo USB", 25)
]

# O objetivo é criar uma lista de strings no formato:
# "Nome: R$ preco"
# Mas apenas para produtos com preco maior ou igual a 100

# Resultado esperado:
# ["Teclado: R$ 120", "Monitor: R$ 900"]

lista_produtos = [
    f"{produto}: R$ {preco}" 
    for produto, preco in produtos 
    if preco >= 100
    ]

print(lista_produtos)