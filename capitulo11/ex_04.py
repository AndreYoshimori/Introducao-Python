# Exercício 11.4: Modifique o programa do exercício 11.3 de forma a perguntar dois valores e
# listar todos os produtos com preços entre esses dois valores.

import sqlite3
from contextlib import closing


with sqlite3.connect("capitulo11/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        preco_min = input("Digite o valor mínimo do intervalo de preços: ")
        preco_max = input("Digite o valor máximo do intervalo de preços: ")

        cursor.execute("select * from precos")

        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            else:
                nome = resultado[0]
                preco = resultado[1]
                if preco_min <= preco <= preco_max:
                    print(nome)
