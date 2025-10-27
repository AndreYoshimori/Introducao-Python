# Exercício 5.13: Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
divida_inicial = float(input('Digite o valor inicial da dívida: '))
divida = divida_inicial
juros = float(input('Digite o juros mensal: '))
juros /= 100
mensal_pago = float(input(f'Qual será o valor pago mensalmente? O valor precisa ser superior a R$ {divida * juros:.2f}.\n->'))
while mensal_pago <= divida * juros:
    mensal_pago = float(input(f'Qual será o valor pago mensalmente? O valor precisa ser superior a R$ {divida * juros:.2f}.\n->'))
meses = 0
total_juros = 0
total_pago = 0
while divida > 0:
    total_juros += divida * juros
    divida += divida * juros
    if divida > mensal_pago:
        divida -= mensal_pago
        total_pago += mensal_pago
    else:
        total_pago += divida
        divida = 0
    meses += 1
print(f'Número de meses para que a dívida seja paga: {meses}\nTotal pago: {total_pago:.2f}\nTotal de juros pago: {total_juros:.2f} ')