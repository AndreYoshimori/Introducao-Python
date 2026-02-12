import sqlite3


print("Região Número de Estados")
print("====== =================")

with sqlite3.connect("capitulo11/brasil.db") as conexao:
    for regiao in conexao.execute("""
        select região, count(*)
        from estados
        group by região"""):
        print("{0:6} {1:17}".format(*regiao))
