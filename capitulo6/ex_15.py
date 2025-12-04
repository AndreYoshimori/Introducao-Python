# Exercício 6.15: Modifique o programa 6.13 de forma a perguntar o número de salas disponíveis no cinema, assim como a quantidade de lugares em cada uma delas.

salas_disponiveis = input('Digite a quantidade de salas disponíveis: ')
while not salas_disponiveis.isnumeric():
    salas_disponiveis = input('Por favor, insira apenas números. Digite a quantidade de salas disponíveis: ')
salas_disponiveis = int(salas_disponiveis)

lugares_vagos = list(range(salas_disponiveis))

for i in range(len(lugares_vagos)):
    entrada = input(f'Digite a quantidade de lugares disponíveis na sala {i + 1}: ')
    while not entrada.isnumeric():
        entrada = input(f'Por favor, insira apenas números. Digite a quantidade de lugares disponíveis na sala {i + 1}: ')
    entrada = int(entrada)
    lugares_vagos[i] = entrada

while True:
    sala = input('Digite o número da sala (0 sai): ')
    while not sala.isnumeric():
        sala = input('Por favor, insira apenas números. Digite o número da sala (0 sai): ')
    sala = int(sala)

    if sala == 0:
        print('Fim')
        break
    elif sala > len(lugares_vagos) or sala < 1:
        print('Sala inválida.')
    elif lugares_vagos[sala - 1] == 0:
        print('Desculpe, sala lotada.')
    else:
        lugares = input(f'Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): ')
        while not lugares.isnumeric():
            lugares = input(f'Por favor, insira apenas números. Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): ')
        lugares = int(lugares)

        if lugares > lugares_vagos[sala - 1]:
            print('Esse número de lugares não está disponível.')
        elif lugares <= 0:
            print('Quantidade inválida.')
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f'{lugares} lugares vendidos na sala {sala}!')

print('Utilização das salas:')
for sala, vagas in enumerate(lugares_vagos):
    print(f'Sala {sala + 1} - {vagas} lugar(es) vazio(s).')