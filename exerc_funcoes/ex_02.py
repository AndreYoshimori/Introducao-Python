# Temos uma lista de notas
# Algumas notas são inválidas (menores que 0 ou maiores que 10)
# O objetivo é criar uma nova lista apenas com as notas válidas

notas = [10, -1, 7, 11, 8, 0, 3]

# Crie a lista notas_validas usando list comprehension
# Considere válidas apenas notas entre 0 e 10 (inclusive)
# Resultado esperado:
# [10, 7, 8, 0, 3]

def valida_nota(nota):
    if nota >= 0 and nota <= 10:
        return True
    return False

notas_validas = [nota for nota in notas if valida_nota(nota)]

print(notas_validas)
