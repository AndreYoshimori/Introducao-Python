# Exercício 9: Dados dois dicionário, retorne uma lista com todas as chaves presentes em ambos.
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

chaves_comuns = []

for chave in dicionario1:
    if chave in dicionario2:
        chaves_comuns.append(chave)

print(f'Chaves presentes em ambos os dicionários: {chaves_comuns}')