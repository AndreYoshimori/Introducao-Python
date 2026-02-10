# Programa 11.1: Consulta com múltiplos resultados

import sqlite3

conexao = sqlite3.connect("capitulo11/agenda.db")
cursor = conexao.cursor()

cursor.execute("select * from agenda")
resultado = cursor.fetchall()

for registro in resultado:
    print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")

cursor.close()
conexao.close()