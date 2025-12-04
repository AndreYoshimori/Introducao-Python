# Exercício 6.6: Modifique o programa para trabalhar com duas filas.
# Para facilitar seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2.
# O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.

ultimo1 = 10
fila1 = list(range(1, ultimo1))

ultimo2 = 6
fila2 = list(range(1, ultimo2))

while True:
    print(f'Fila 1 atual: {fila1}')
    print(f'Fila 2 atual: {fila2}')
    print(f'Digite F ou G para adicionar um cliente ao fim da lista 1 ou 2, respectivamente.\nA ou B para realizar o atendimento da fila 1 ou 2, respectivamente.\nS para sair.')

    operacao = input('Operação (F, G, A, B, S): ')

    i = 0
    while i < len(operacao):
        if operacao[i] == 'A':
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f'Cliente {atendido} atendido na fila 1.')
            else:
                print('Fila 1 vazia! Ninguém para atender.')
        elif operacao[i] == 'B':
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f'Cliente {atendido} atendido na fila 2.')
            else:
                print('Fila 2 vazia! Ninguém para atender.')
        elif operacao[i] == 'F':
            fila1.append(ultimo1)
            ultimo1 += 1
        elif operacao[i] == 'G':
            fila2.append(ultimo2)
            ultimo2 += 1
        elif operacao[i] == 'S':
            break
        else:
            print('Operação inválida! Digite apenas F, G, A, B, ou S!')

        i += 1
        
    if 'S' in operacao:
        break