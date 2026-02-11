# Programa 11.5: Consulta utilizando parâmetros

import sqlite3
from contextlib import closing


nome = input(("Nome a selecionar: "))

with sqlite3.connect("capitulo11/agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = ?", (nome,))

        x = 0

        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if not x:
                    print("Nada encontrado")
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
            x += 1