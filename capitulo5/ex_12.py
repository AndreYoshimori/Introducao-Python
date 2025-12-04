# Exercício 5.12: Altere o programa anterior de forma a perguntar também qual o valor depositado mensalmente.
# Esse valor será depositado no início de cada mês e você deve considerá-lo para o cálculo de juros do mês seguinte

deposito_inicial = float(input('Digite quanto você deseja depositar na sua poupança: '))
poupanca = deposito_inicial
juros = float(input('Digite a taxa de juros: '))
juros /= 100
deposito_mensal = float(input('Digite quanto dinheiro vai ser depositado mensalmente: '))
meses = 24

i = 1
while i <= meses:
    poupanca += poupanca * juros
    poupanca += deposito_mensal
    print(f'Mês {i}: R$ {poupanca:.2f}')
    i += 1

total_investido = deposito_inicial + deposito_mensal * meses
ganho = poupanca - total_investido

print(f'O total ganho com juros nesse período de {24} meses foi R$ {ganho:.2f}')