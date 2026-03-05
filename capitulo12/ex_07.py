# Escreva um programa que valide a entrada de dados do usuário. 
# O programa deve aceitar números de CPF no seguinte formato: 999.999.999-99, em que cada 9 representa um dígito.
# Exija os pontos e o traço no final, verificando a correta quantidade de dígitos.


import re


while True:
    entrada = input("CPF: ")

    if re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", entrada):
        print("CPF válido!")
        break
    else:
        print("CPF inválido.")
