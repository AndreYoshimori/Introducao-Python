# Exercício 7.6: Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pela terceira.
# 1ª string: AATTCGAA
# 2ª string: TG
# 3ª string: AC
# Resultado: AAAACCAA

primeira = 'AATTCGAA'
lista_primeira = list(primeira)
segunda = 'TG'
terceira = 'AC'

for i in range(len(lista_primeira)):
    for j in range(len(segunda)):
        if lista_primeira[i] == segunda[j]:
            lista_primeira[i] = terceira[j]

primeira = "".join(lista_primeira)

print(primeira)