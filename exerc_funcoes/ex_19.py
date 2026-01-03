# Crie uma função que receba um multiplicador
# e vários números, retornando uma lista
# com todos os números multiplicados

# Exemplo:
# multiplica(2, 1, 2, 3) -> [2, 4, 6]

def multiplica(multiplicador, *args):
    multiplicados = [n * multiplicador for n in args]
    return multiplicados

print(multiplica(5, 2, 3, 4, 5, 6, 7))