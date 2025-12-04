# Exercício 6.11: Modifique o Programa 6.6 usando for.
# Explique por que nem todos os while podem ser transformados em for.

L = []

while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        break
    L.append(n)
    
for elem in L:
    print(elem)

# R: O primeiro while não pode ser transformado em for porque o número de repetições deve ser indefinido, uma vez que o intuito do programa é o usuário poder digitar quantos números
# quiser e só finalizar o programa quando desejar.