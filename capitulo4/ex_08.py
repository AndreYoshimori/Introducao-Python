# Exercício 4.8: Reescreva o Programa 4.4 e calcule a conta da operadora Tchau usando else
'''
plano = input('qual é o seu plano de celular?')
if plano == 'falapouco':
    minutos_no_plano = 100
    extra = 0.20
    preco = 50
if plano == 'falamuito':
    minutos_no_plano = 500
    extra = 0.15
    preco = 99
if plano !='falopouco' and plano != 'falomuito':
    print('Não conheço este plano.')
'''

plano = input('Digite seu plano de celular: ')
if plano == 'falapouco':
    minutos_no_plano = 100
    extra = 0.20
    preco = 50
elif plano == 'falamuito':
    minutos_no_plano = 500
    extra = 0.15
    preco = 99
else:
    print('Não conheço este plano.')
if plano == 'falapouco' or plano == 'falamuito':
    minutos_consumidos = input('Digite quantos minutos você consumiu?')
    while not minutos_consumidos.isnumeric():
        minutos_consumidos = input('Digite quantos minutos você consumiu?')
    minutos_consumidos = int(minutos_consumidos)
    print('Você vai pagar:')
    print(f'Preço do plano R$ {preco:.2f}.')
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f'Suplemento R$ {suplemento:.2f}.')
    print(f'Total R$ {(preco + suplemento):.2f}.')