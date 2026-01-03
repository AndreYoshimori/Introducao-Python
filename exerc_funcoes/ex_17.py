# Crie uma função que receba vários números
# e retorne a média deles

# Exemplo:
# media(2, 4, 6) -> 4

def media(*args):
    soma = sum(args)
    media = soma / len(args)
    return media

print(media(2, 4, 6))