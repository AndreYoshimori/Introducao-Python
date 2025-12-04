# Exercício 5: Crie uma lista com os números de 1 a 50.
# Depois, crie uma nova lista contendo apenas os números que são primos.

numeros = list(range(1, 51))

primos = []

for elem in numeros:
    if elem == 1:
        continue
    else:
        limite = elem ** 0.5
        div = 2
        while div <= limite:
            if elem % div == 0:
                break
            div += 1
        else:
            primos.append(elem)
      
print(f'Números primos de 1 a 50: {primos}')