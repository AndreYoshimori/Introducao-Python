# Exercício 7.5: Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
# 1ª string: AATTGGAA
# 2ª string: TG
# 3ª string: AAAA

primeira = 'AATTGGAA'
lista_primeira = list(primeira)
segunda = 'TG'

for caractere in segunda:
    i = 0
    while i < len(lista_primeira):
        if caractere != lista_primeira[i]:
            i += 1
        else:
            del lista_primeira[i]

terceira = "".join(lista_primeira)

print(terceira)
