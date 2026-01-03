import string

# Temos uma lista de nomes com espaços extras e letras fora do padrão
# O objetivo é criar uma nova lista com os nomes:
# - sem espaços no começo e no fim
# - com a primeira letra maiúscula e o restante minúsculo

nomes = ["  aNdrÉ  ", "maria", " JOÃO", "aNa  "]

# Crie a lista nomes_ok usando list comprehension
# Resultado esperado:
# ["André", "Maria", "João", "Ana"]

def ajusta_nome(nome):
    nome = nome.strip().title()
    return nome

nomes_ok = [ajusta_nome(nome) for nome in nomes]

print(nomes_ok)