# Exercício 12.1: Modifique o programa anterior para reconhecer sequências de letras.
# Uma letra é um caractere entre A e Z ou entre a e z, considerando letras maiúsculas e minúsculas.
# Ignore caracteres acentuados.
# Imprima uma lista com as sequências de letras encontradas.

entrada = "ABC431DEF901c431203FXEW9"

saida = []
palavra = []

for caractere in entrada:
    if "A" <= caractere <= "z":
        if not palavra:
            saida.append(palavra)
        palavra += caractere
    elif palavra:
        palavra = []
    
for encontrado in saida:
    print("".join(encontrado))
    