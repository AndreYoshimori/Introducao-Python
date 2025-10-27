# Execute o Programa 5.16 para os seguintes valores: 501, 745, 384, 2, 7 e 1.
a_pagar = input('Digite o valor a pagar: ')
while not a_pagar.isnumeric():
    a_pagar = input('Digite o valor a pagar: ')
a_pagar = int(a_pagar)
cedulas = 0
cedula_atual = 50
while True:
    if cedula_atual <= a_pagar:
        a_pagar -= cedula_atual
        cedulas += 1
    else:
        print(f'{cedulas} cédulas de R$ {cedula_atual}.')
        if a_pagar == 0:
            break
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 5
        elif cedula_atual == 5:
            cedula_atual = 1
        cedulas = 0