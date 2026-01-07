# Temos um dicionário de preços em reais
precos = {
    "Teclado": 120,
    "Mouse": 80,
    "Monitor": 900
}

# Crie um novo dicionário aplicando 10% de desconto
# em todos os produtos

# Resultado esperado:
# {"Teclado": 108.0, "Mouse": 72.0, "Monitor": 810.0}

com_desconto = {
    produto: preco * 0.9 
    for produto, preco in precos.items()
    }

print(com_desconto)
