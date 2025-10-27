# Exercício 4.7: Analise o Programa 4.3. Faz sentido usar o else nesse programa? Explique sua resposta.
# Programa 4.3
salario = float(input('Digite o salário para cálculo do imposto: '))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f'Salário: R$ {salario:6.2f} Imposto a pagar: R$ {imposto:6.2f}')

# R: Não, nesse programa não faz sentido usar o else porque mesmo que o valor inserido passe pela primeira condição, ele
# ainda deve ser testado pela segunda, uma vez que são cálculos complementares. Ou seja, as duas condições podem ser
# verdadeiras em uma mesma vez.