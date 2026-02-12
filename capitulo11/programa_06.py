# Programa 11.6: Exemplo de update sem where e com rowcount

import sqlite3
from contextlib import closing

with sqlite3.connect("capitulo11/agenda_copy.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""update agenda
                              set telefone = '12345-6789' """)
        
        print("Registros alterados: ", cursor.rowcount)
