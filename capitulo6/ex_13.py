# Exercício 6.13: A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
# Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]

maxima = T[0]
minima = T[0]

media = 0

for elem in T:
    if elem > maxima:
        maxima = elem
    elif elem < minima:
        minima = elem
    media += elem
    
media /= len(T)

print(f'A maior temperatura foi {maxima:.0f}°.')
print(f'A menor temperatura foi {minima:.0f}°.')
print(f'A temperatura média foi {media:.0f}°')