# Exercício 12.9: Escreva um programa que valide a entrada de dados do usuário.
# Tente achar um número válido de CPF ou de CNPJ como definido nos exercícios anteriores.
# Exiba uma mensagem dizendo se o número é válido e se este é um CNPJ ou um CPF.

import re


cpf_regex = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")
cnpj_regex = re.compile(r"\d{2}\.\d{3}\.\d{3}/?\d{4}-\d{2}")

while True:
    entrada = input("Digite seu CPF ou CNPJ: ")

    if cpf_regex.fullmatch(entrada):
        print("CPF válido!")
        break
    elif cnpj_regex.fullmatch(entrada):
        print("CNPJ válido!")
        break
    else:
        print("Entrada inválida.")
