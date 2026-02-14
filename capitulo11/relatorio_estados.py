import sqlite3


print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")

with sqlite3.connect("capitulo11/brasil.db") as conexao:
    for região in conexao.execute("""
        select região, count(*), min(população), 
               max(população), avg(população), 
               sum(população) as tpop
        from estados
        group by região
        order by tpop desc  """):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))

    print("\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
        *conexao.execute("""
            select count(*), min(população), max(população),
                   avg(população), sum(população) from estados""").fetchone()
    ))
    