# Exercício 3.12: Escreva um programa que calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist =int(input('Digite a distância a ser percorrida: '))
vel = int(input('Digite a valocidade média que pretende manter, em km/h: '))
tempo = dist / vel

print(f'A viagem durará {tempo} hora(s).')
