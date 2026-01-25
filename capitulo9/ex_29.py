# Exercício 9.29: Modifique o Programa 9.8 para utilizar o elemento p em vez de h2 nos filmes.

filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora"]
}

with open("capitulo9/filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
    
    for c, v in filmes.items():
        pagina.write(f"<h1>{c}</h1>\n")
        for e in v:
            pagina.write(f"<p>{e}</p>\n")

    pagina.write("</body>\n")
    pagina.write("</html>\n")