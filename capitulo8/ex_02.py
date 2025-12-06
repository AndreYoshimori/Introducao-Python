# Exercício 8.2: Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
# Valores esperados:
# multiplo(8, 4) == True
# multiplo(7, 3) == False
# multiplo(5, 5) == True

def multiplo(numero1, numero2):
    return numero1 % numero2 == 0

num1 = 8
num2 = 4

if multiplo(num1, num2):
    print(f'{num1} é múltiplo de {num2}')
else:
    print(f'{num1} não é múltiplo de {num2}')