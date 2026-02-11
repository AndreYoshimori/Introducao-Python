# Exercício 11.3: Escreva um programa que realize consultas do banco de dados preços.db, criado no exercício 11.1;
# O programa deve perguntar o nome do produto e listar seu preço.

import sqlite3
from contextlib import closing


with sqlite3.connect("capitulo11/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        while True:
            nome = input("Digite o nome de um produto para consultar seu preço ou 0 para finalizar: ")

            if nome == "0":
                break
            else:
                cursor.execute("select preco from precos where nome = ?", (nome,))
                resultado = cursor.fetchone()
                if resultado is None:
                    print("Produto não encontrado.")
                else:
                    print(resultado)
