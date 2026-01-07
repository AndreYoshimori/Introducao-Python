# Exercício 7.3: Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
# 1ª string: CTA
# 2ª string: ABC
# 3ª string: BT
# A ordem dos caracteres da terceira string não é importante.

primeira = 'CTA'
segunda = 'ABC'

distintas = []

for i in range(len(primeira)):
    if primeira[i] not in segunda and primeira[i] not in distintas:
        distintas.append(primeira[i])

for i in range(len(segunda)):
    if segunda[i] not in primeira and segunda[i] not in distintas:
        distintas.append(segunda[i])

terceira = ''.join(distintas)

print(terceira)
