import sqlite3
from contextlib import closing


dados = [
    ["São Paulo", 43663672],
    ["Minas Gerais", 20593366],
    ["Rio de Janeiro", 16369178],
    ["Bahia", 15044127],
    ["Rio Grande do Sul", 11164050],
    ["Paraná", 10997462],
    ["Pernambuco", 9208511],
    ["Ceará", 8778575],
    ["Pará", 7969655],
    ["Maranhão", 6794298],
    ["Santa Catarina", 6634250],
    ["Goiás", 6434052],
    ["Paraíba", 3914418],
    ["Espírito Santo", 3838363],
    ["Amazonas", 3807923],
    ["Rio Grande do Norte", 3373960],
    ["Alagoas", 3300938],
    ["Piauí", 3184165],
    ["Mato Grosso", 3182114],
    ["Distrito Federal", 2789761],
    ["Mato Grosso do Sul", 2587267],
    ["Sergipe", 2195662],
    ["Rondônia", 1728214],
    ["Tocantins", 1478163],
    ["Acre", 776463],
    ["Amapá", 734995],
    ["Roraima", 488072]
]

with sqlite3.connect("capitulo11/brasil.db") as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""
            create table estados(
                id integer primary key autoincrement,
                nome text,
                população integer
            )
        """)

        cursor.executemany("insert into estados(nome, população) values(?,?)", dados)

    conexao.commit()
