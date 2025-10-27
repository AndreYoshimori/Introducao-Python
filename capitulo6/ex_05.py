# Exercício 6.5: Altere o programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez.
# Atualmente, apenas um comando pode ser inserido por vez.
# Altere-o de forma a considerar operação como uma string.
# Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente a saída do programa.
ultimo = 10
fila = list(range(1, ultimo))
while True:
    print(f'Existem {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print(f'Digite F para adicionar um cliente ao fim da lista, ou A para realizar o atendimento. S para sair.')
    operacao = input('Operação (F, A, S): ')
    i = 0
    while i < len(operacao):
        if operacao[i] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido.')
            else:
                print('Fila vazia! Ninguém para atender.')
        elif operacao[i] == 'F':
            fila.append(ultimo)
            ultimo += 1
        elif operacao[i] == 'S':
            break
        else:
            print('Operação inválida! Digite apenas F, A OU S!')
        i += 1
    if 'S' in operacao:
        break    