# Exercício 10: Dados dois dicionário, retorne uma lista com as chaves que não são comuns aos dois.

dicionario1 = {
    'nome': 'Carlos',
    'idade': 25,
    'cidade': 'São Paulo',
    'profissão': 'Engenheiro'
}

dicionario2 = {
    'nome': 'Ana',
    'idade': 30,
    'pais': 'Brasil',
    'profissão': 'Médica'
}

chaves_diferentes = []

for chave in dicionario1:
    if chave not in dicionario2:
        chaves_diferentes.append(chave)

for chave in dicionario2:
    if chave not in dicionario1:
        chaves_diferentes.append(chave)

print(f'Chaves que não são comuns aos dois: {chaves_diferentes}')