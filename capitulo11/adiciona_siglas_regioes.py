import sqlite3

with sqlite3.connect("capitulo11/brasil.db") as conexao:
    conexao.execute("""alter table estados
                       add sigle text""")
    
    conexao.execute("""alter table estados
                       add região text""")
    