# Exercício 8.3: Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado**2).
# Valores esperados:
# área_quadrado(4) == 16
# área_quadrado(9) == 81

def area_quadrado(tamanho_lado):
    area = tamanho_lado ** 2
    return area

tamanho_lado = 4

area = area_quadrado(tamanho_lado)

print(f'Um quadrado com {tamanho_lado} de lado, possui {area} de área.')
