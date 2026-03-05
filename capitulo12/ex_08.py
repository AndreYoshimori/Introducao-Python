# Escreva um programa que valide a entrada de dados do usuário.
# O programa deve aceitar números de CNPJ no seguinte formato: 99.999.999/9999-99, em que cada 9 representa um dígito.
# Exija os pontos e o traço no final, verificando a correta quantidade de dígitos.

import re


while True:
    entrada = input("CNPJ: ")

    if re.fullmatch(r"\d{2}\.\d{3}\.\d{3}/?\d{4}-\d{2}", entrada):
        print("CNPJ válido!")
        break
    else:
        print("CNPJ inválido")
