# Exercício 4.6: Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45, para viagens mais longas.

dist = input('Digite a distância que vc pretende percorrer em km: ')
while not dist.isnumeric():
    dist = input('Digite a distância que vc pretende percorrer em km:')
dist = int(dist)

if dist <= 200:
    valor_km = 0.50
    preco = dist * valor_km
    print(f'O valor da passagem é R$ {preco}.')
else:
    valor_km = 0.45
    preco = dist * valor_km
    print(f'O valor da passagem é R$ {preco}.')