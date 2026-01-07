# Temos listas de tamanhos diferentes

nomes = ["Ana", "Bruno", "Carlos", "Daniela"]
idades = [20, 25]

# Use zip para criar uma lista de strings no formato:
# "Nome - Idade"

# Resultado esperado:
# ["Ana - 20", "Bruno - 25"]

nome_e_idade = [f"{nome} - {idade}" for nome, idade in zip(nomes, idades)]

print(nome_e_idade)
