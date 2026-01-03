# Reescreva o exercício 3 usando list comprehension
# Compare qual versão você acha mais legível

numeros = [1, 2, 3, 4, 5, 6]

resultado = [n * 2 for n in numeros if n % 2 == 0]

print(resultado)

# R: Com certeza o list comprehension é a versão mais legível.