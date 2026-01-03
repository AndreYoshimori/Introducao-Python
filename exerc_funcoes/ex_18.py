# Crie uma função que receba dados de um usuário via kwargs
# e imprima no formato:
# chave: valor

# Exemplo:
# exibe_usuario(nome="Ana", idade=20)

def exibe_usuario(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

exibe_usuario(nome="Ana", idade=20)