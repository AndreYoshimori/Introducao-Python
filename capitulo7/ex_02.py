# Exercício 7.2: Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
# 1ª string: AAACTBF
# 2ª STRING: CBTO
# Resultado: CBT
# A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.
primeira = 'AAACTBF'
segunda = 'CBTO'
comuns = []
for i in range(len(primeira)):
    if primeira[i] in segunda and primeira[i] not in comuns:
        comuns.append(primeira[i])
terceira = ''.join(comuns)
print(terceira)