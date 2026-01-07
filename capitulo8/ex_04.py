# Exercício 8.4: Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x alture) / 2).
# Valores esperados:
# área_triângulo(6, 9) == 27
# área_triângulo(5, 8) == 20

def area_triangulo(tamanho_base, tamanho_altura):
    area = (tamanho_base * tamanho_altura) / 2
    return area

tamanho_base = 6
tamanho_altura = 9

area = area_triangulo(tamanho_base, tamanho_altura)

print(f'A área de um triângulo com {tamanho_base} de base e {tamanho_altura} de altura é {area}')
