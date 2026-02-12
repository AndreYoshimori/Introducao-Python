import sqlite3


with sqlite3.connect("capitulo11/brasil.db") as conexao:
    conexao.row_factory = sqlite3.Row

    print(f"{'Id':3s} {'Estado':<20s} {'População':12s}")
    print("=" * 37)

    for estado in conexao.execute("select * from estados order by população desc"):
        print(f"{estado['id']:3d} {estado['nome']:<20s} {estado['população']:>12,}")
