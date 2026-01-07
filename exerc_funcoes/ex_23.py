# Temos uma lista de nomes com espaços extras
nomes = ["  Ana ", " ", "Bruno", "  ", "Carlos  "]

# Crie uma lista apenas com os nomes válidos (não vazios),
# já normalizados (strip)

nomes_validos = [
    nome_normalizado 
    for nome in nomes 
    if (nome_normalizado := nome.strip())
    ]

print(nomes_validos)
