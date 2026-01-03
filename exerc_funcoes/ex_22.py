# Temos uma lista de idades em texto
idades = ["18", "21", "abc", "30", ""]

# Crie uma lista apenas com as idades válidas (int >= 18)
# Use walrus para converter a idade uma única vez

idades_validas = [
    idade_int 
    for idade in idades 
    if idade.isnumeric() and (idade_int := int(idade)) >= 18
    ]

print(idades_validas)