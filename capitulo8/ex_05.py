# Exercício 8.5: Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista, vistos no Capítulo 7.

def pesquise(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return None

L = [10, 20, 25, 30]

print(pesquise(L, 25))
print(pesquise(L, 27))