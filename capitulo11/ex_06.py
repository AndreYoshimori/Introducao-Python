# Exercício 11.6: Escreva um programa que pergunte o nome do produto e um novo preço.
# Usando o banco preços.db, atualize o preço desse produto no banco de dados.

import sqlite3
from contextlib import closing

nome_produto = input("Digite o nome do produto que deseja atualizar o preço: ")
novo_preco = float(input("Digite o novo preço: "))

with sqlite3.connect("capitulo11/precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''update precos
                              set preco = ?
                              where nome = ?''', (novo_preco, nome_produto))
        
        if cursor.rowcount > 0:
            print("Alteração concluída.")
        else:
            print("Produto não encontrado.")
