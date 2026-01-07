# Exercício 6.12: Altere o programa 6.11 de forma a imprimir o menor elemento da lista.

L = [10, 7, 2, 4]

minimo = L[0]

for elem in L:
    if elem < minimo:
        minimo = elem        
             
print(minimo)
