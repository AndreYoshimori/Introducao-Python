# Exercício 6.17: O que acontece quando dois valores são iguais? Rastreie o Programa 6.20, mas com a lista = L = [3, 3, 1, 5, 4]

L = [3, 3, 1, 5, 4]

fim = len(L)

while fim > 1:
    trocou = False
    
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
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

# R: Nada, a troca só ocorre quando um número é maior que o à sua direita. Ou seja, na comparação entre números iguais, eles vão continuar na mesma posição.
