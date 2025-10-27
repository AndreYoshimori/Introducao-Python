# Exercício 3.13: Escreva um programa que converta uma temperatura digitada em °C em °F. 
# A fórmula para essa conversão é F = 9 * C / 5 + 32
temp_celsius = int(input('Digite uma temperatura em °C: '))
temp_farenheit = 9 * temp_celsius / 5 + 32
print(f'{temp_celsius}°C em farenheit são {temp_farenheit}°F.')