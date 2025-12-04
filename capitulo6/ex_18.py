# Exercício 6.18: Modifique o Programa 6.20 para ordenar a lista em ordem decrescente.
# L = [1, 2, 3, 4, 5] deve ser ordenada como L = [5, 4, 3, 2, 1].

L = [1, 2, 3, 4, 5]

fim = len(L)

while fim > 1:
    trocou = False
    
    x = 0
    while x < (fim - 1):
        if L[x] < L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1

for elem in L:
    print(elem)