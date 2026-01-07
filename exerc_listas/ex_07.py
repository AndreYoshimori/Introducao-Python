# Exercício 7: Crie uma lista com 10 números aleatórios entre 1 e 100 (use a biblioteca random).
# Depois, mostre a lista original e uma nova lista ordenada sem alterar a original.

import random


lista = random.sample(range(1, 101), 10)

print(lista)
print(sorted(lista))
