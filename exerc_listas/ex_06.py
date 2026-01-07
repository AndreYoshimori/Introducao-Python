# Exercício 6: Peça ao usuário uma lista de nomes (1 por linha).
# O usuário digita "fim" para encerrar.
# Depois, peça uma letra e imprima todos os nomes que começam com essa letra.

nomes = []

while True:
    nome = input('Digite um nome ou "fim" para encerrar: ')
    if nome == 'fim':
        break
    nomes.append(nome)
    
letra = input('Digite uma letra para ver os nomes da lista que começam com ela: ')
for elem in nomes:
    if elem[0] == letra:
        print(elem)
        