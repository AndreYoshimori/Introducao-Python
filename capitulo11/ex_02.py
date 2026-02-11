# Exercício 11.2: Faça um programa para listar todos os preços do banco preços.db.

import sqlite3
from contextlib import closing


with sqlite3.connect("capitulo11/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select preco from precos")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(resultado)
