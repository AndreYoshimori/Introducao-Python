# Exercício 6.14: Modifique o Programa 6.13 de forma a mostrar quantos ingressos foram vendidos em cada sala.
# Utilize uma lista do mesmo tamanho da quantidade de salas e utilize seus elementos para contar quantos ingressos foram vendidos em cada sala.
# Imprima na tela o total das vendas no fim do programa.
lugares_vagos = [10, 4, 7, 5, 8]
ingressos_vendidos = [0, 0, 0, 0, 0]
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
            lugares = input(f'Por favor, insira apenas números. Digite um número. Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): ')
        lugares = int(lugares)
        if lugares > lugares_vagos[sala - 1]:
            print('Esse número de lugares não está disponível.')
        elif lugares <= 0:
            print('Quantidade inválida.')
        else:
            lugares_vagos[sala - 1] -= lugares
            ingressos_vendidos[sala - 1] += lugares
            print(f'{lugares} lugar(es) vendido(s) na sala {sala}!')
print('Utilização das salas:')
for sala, vagas in enumerate(lugares_vagos):
    print(f'Sala {sala + 1} - {vagas} lugar(es) vazio(s).')
for sala, vendidos in enumerate(ingressos_vendidos):
    print(f'Sala {sala + 1} - {vendidos} ingresso(s) vendido(s).')