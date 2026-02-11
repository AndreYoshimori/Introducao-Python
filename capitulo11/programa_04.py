# Programa 11.4: Consulta com filtro de seleção

import sqlite3
from contextlib import closing


with sqlite3.connect("capitulo11/agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = 'Nilo'")

        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
            