# Temos duas listas de vendas
# Cada posição representa o mesmo dia

vendas_loja1 = [100, 200, 150]
vendas_loja2 = [80, 220, 130]

# Crie uma lista com o total de vendas por dia
# somando os valores das duas lojas

# Resultado esperado:
# [180, 420, 280]

total_dia = [
    venda1 + venda2 
    for venda1, venda2 in zip(vendas_loja1, vendas_loja2)
    ]

print(total_dia)