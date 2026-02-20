# Programa 12.1: Procura sequências de algarismos

entrada = "ABC431DEF901c431203FXEW9"

saida = []
numero = []

for caractere in entrada:
    if "0" <= caractere <= "9":
        if not numero:
            saida.append(numero)
        numero += caractere
    elif numero:
        numero = []
    
for encontrado in saida:
    print("".join(encontrado))