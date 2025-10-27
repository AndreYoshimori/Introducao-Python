# Exercício 6.16: O que acontece quando a lista já está ordenada? Rastreie o Programa 6.20, mas com a lista L = [1, 2, 3, 4, 5].
L = [1, 2, 3, 4, 5]
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
# R: O programa vai finalizar após o primeiro ciclo, uma vez que não houve nenhuma troca, e assim "trocou" continuou sendo False, acionando o break.