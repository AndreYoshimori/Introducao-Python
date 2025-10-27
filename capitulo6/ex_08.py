# Exercício 6.8: Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou.
# Dica: observe a condição de saída do while.
L = [15, 7, 27, 39]
v = input('Digite o valor a procurar: ')
while not v.isnumeric():
    v = input('Por favor, insira apenas números. Digite o valor a procurar: ')
v = int(v)
i = 0
while i < len(L):
    if L[i] == v:
        print(f'{v} encontrado na posição {i + 1}')
        break
    i += 1
else:
    print(f'{v} não encontrado.')