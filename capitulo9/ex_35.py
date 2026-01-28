# Exercício 9.35: Utilizando a função os.walk, crie uma página HTML com o nome e 
# tamanho de cada arquivo de um diretório passado e de seus subdiretórios.

import sys
from pathlib import Path
import os.path


caminho_entrada = Path(sys.argv[1])
caminho_saida = Path("capitulo9/tamanho_arquivos.html")

with caminho_saida.open("w", encoding="utf-8") as pagina:
    pagina.write("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Imagens</title>
</head>
<body>
""")

    for raiz, _, arquivos in caminho_entrada.walk():
        for f in arquivos:
            caminho = raiz / f
            tamanho = os.path.getsize(caminho)
            pagina.write(f"<p>Arquivo: {f} | Tamanho: {tamanho} bytes</p>\n")

    pagina.write("</body>\n")
    pagina.write("</html>\n")