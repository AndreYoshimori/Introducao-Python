# Exercício 4.2: Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = (input('Digite a velocidade do seu carro: '))
while not velocidade.isnumeric():
    velocidade = (input('Digite a velocidade do seu carro: '))
velocidade = int(velocidade)

velocidade_via = 80
valor_multa_por_km = 5

if velocidade > velocidade_via:
    velocidade_excedida = velocidade - velocidade_via
    multa = velocidade_excedida * valor_multa_por_km
    print(f'Você foi multado em R$ {multa}.')
else:
    print('Você não foi multado.')
    
