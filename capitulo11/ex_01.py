# Exercício 11.1: Faça um programa que crie o banco de dados preços.db com a tabela preços para armazenar uma lista de preços de venda de produtos.
# A tabela deve conter o nome do produto e seu respectivo preço.
# O programa também deve inserir alguns dados para teste.

import sqlite3
from contextlib import closing


dados = [("Escova de dente", 10.00), 
         ("Café", 20.00), 
         ("Arroz", 15.00)]

with sqlite3.connect("capitulo11/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
                create table precos(
                    nome text, 
                    preco real)
                ''')
        
        cursor.executemany('''
                insert into precos (nome, preco)
                values(?, ?)
                ''', dados)
