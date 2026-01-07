# Exercício 7.7: Escreva um programa que peça ao usuário que digite uma frase e imprima quantas vogais ela contém.
# Não considere maiúsculas e minúsculas como diferentes.
# Exemplo: uma frase como "A casa" deve imprimir três "as".

vogais = ['a', 'e', 'i', 'o', 'u']

frase = input('Digite uma frase para ver quantas vogais ela contém: ')
frase = frase.lower()

vogais_presentes = []

for letra in frase:
    if letra in vogais:
        vogais_presentes.append(letra)

frase_vogais = "".join(vogais_presentes)

print(frase_vogais)
