# Exercício 11.5: Escreva um programa que aumente o preço de todos os produtos do banco preços.db em 10%.

import sqlite3
from contextlib import closing

with sqlite3.connect("capitulo11/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''update precos
                              set preco = preco * 1.1''')
