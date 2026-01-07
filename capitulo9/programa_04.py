# Programa 9.4: Gravação de números pares e impares em arquivos diferentes. with em uma só linha.

with open("dados/pares.txt", "w") as pares, open("dados/impares.txt", "w") as impares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f'{n}\n')
        else:
            impares.write(f'{n}\n')
            