# Exercício 5.19: Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01, 0,02, 0,05, 0,10, 0,50.

a_pagar = float(input('Digite o valor a pagar.'))
a_pagar *= 100
cedulas = 0
cedula_atual = 10000

while True:
    if cedula_atual <= a_pagar:
        a_pagar -= cedula_atual
        cedulas += 1
    else:
        print(f'{cedulas} cédulas de R$ {cedula_atual / 100:.2f}.')
        if a_pagar == 0:
            break
        elif cedula_atual == 10000:
            cedula_atual = 5000
        elif cedula_atual == 5000:
            cedula_atual = 2000
        elif cedula_atual == 2000:
            cedula_atual = 1000
        elif cedula_atual == 1000:
            cedula_atual = 500
        elif cedula_atual == 500:
            cedula_atual = 100
        elif cedula_atual == 100:
            cedula_atual = 50
        elif cedula_atual == 50:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 5
        elif cedula_atual == 5:
            cedula_atual = 2
        elif cedula_atual == 2:
            cedula_atual = 1
        cedulas = 0