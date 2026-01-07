# Temos uma função que formata um nome

def formata_nome(nome, sobrenome):
    return f"{nome} {sobrenome}"

# E um dicionário com dados
dados = {"nome": "Ana", "sobrenome": "Silva"}

# Use desempacotamento para chamar a função

resultado = formata_nome(**dados)
print(resultado)
