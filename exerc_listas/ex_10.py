# Exercício 10: Crie uma lista com várias palavras.
# Depois, remova todas as palavras que tenham menos de 4 letras.
palavras = ['maçã', 'banana', 'lua', 'caderno', 'planta', 'sol']
i = 0
while i < len(palavras):
    if len(palavras[i]) < 4:
        del palavras[i]
    else:
        i += 1
print(palavras)