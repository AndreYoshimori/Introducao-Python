# Programa 9.7: Criação de uma página inicial em Python

with open("capitulo9/pagina.html", "w", encoding="utf-8") as pagina:
    pagina.write("<DOCTYPE html>\n")
    pagina.write("<html lang=\"pt-BR\">\n")
    pagina.write("<head>\n")
    pagina.write("<meta charset=\"utf-8\">\n")
    pagina.write("<title>Título da Página</title>\n")
    pagina.write("</head>\n")
    pagina.write("<body>\n")
    pagina.write("Olá!\n")
    for linha in range(100):
        pagina.write(f"<p>{linha}</p>\n")
    pagina.write("</body>\n")
    pagina.write("</html>\n")
    