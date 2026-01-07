# Exercício 5.11: Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.

deposito_inicial = float(input('Digite quanto você deseja depositar na sua poupança: '))
juros = float(input('Digite a taxa de juros: '))
juros = juros / 100
meses = 24
poupanca = deposito_inicial

i = 1
while i <= meses:
    poupanca += poupanca * juros
    print(f'Mês {i}: R$ {poupanca:.2f}')
    i += 1
    
ganho = poupanca - deposito_inicial

print(f'O total ganho com juros nesse período de {24} meses foi R$ {ganho:.2f}')
