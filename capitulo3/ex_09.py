# Exercício 3.9: Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos
dias = 5
horas = 64
minutos = 300
segundos = 800
total_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print(f'O total de {dias} dias, {horas} horas, {minutos} minutos, somados com {segundos} segundos, em segundos, são {total_segundos} segundos.')