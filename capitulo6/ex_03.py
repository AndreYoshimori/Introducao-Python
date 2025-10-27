# Exercício 6.3: Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
L1 = [1, 2, 3, 4]
L2 = [4, 5, 3, 2]
L3 = []
x = 0
while x < len(L1):
    if not L1[x] in L3:
        L3.append(L1[x])
    x += 1

x = 0
while x < len(L2):
    if not L2[x] in L3:
        L3.append(L2[x])
    x += 1

L3