# Exercício 5.20: O que acontece se digitarmos 0,001 no programa anterior? Caso ele não funcione, altere-o de forma a corrigir o problema.

a_pagar = float(input('Digite o valor a pagar: '))
a_pagar *= 1000
cedulas = 0
cedula_atual = 100000

while True:
    if cedula_atual <= a_pagar:
        a_pagar -= cedula_atual
        cedulas += 1
    else:
        print(f'{cedulas} cédulas de R$ {cedula_atual / 1000:.3f}.')
        if a_pagar == 0:
            break
        elif cedula_atual == 100000:
            cedula_atual = 50000
        elif cedula_atual == 50000:
            cedula_atual = 20000
        elif cedula_atual == 20000:
            cedula_atual = 10000
        elif cedula_atual == 10000:
            cedula_atual = 5000
        elif cedula_atual == 5000:
            cedula_atual = 1000
        elif cedula_atual == 1000:
            cedula_atual = 500
        elif cedula_atual == 500:
            cedula_atual = 100
        elif cedula_atual == 100:
            cedula_atual = 50
        elif cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        cedulas = 0
        