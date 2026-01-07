# Exercício 9.3: Crie um programa que leia os arquivos pares.txt e impares.txt e que crie um só arquivo paresimpares.txt 
# com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica.

with open("dados/pares.txt", "r") as pares, open("dados/impares.txt", "r") as impares, open("dados/paresimpares.txt", "w") as paresimpares:
    for par, impar in zip(pares, impares):
        paresimpares.write(par)
        paresimpares.write(impar)
        