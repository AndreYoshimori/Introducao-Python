# Exercício 9.36: Utilizando a função os.walk, crie um programa que calcule o espaço 
# ocupado por diretório e subdiretório, gerando uma página HTML com os resultados.

import sys
from pathlib import Path
import os.path


caminho_entrada = Path(sys.argv[1])

diretorio_script = Path(sys.argv[0]).parent
nome_arquivo_saida = "tamanho_diretorios.html"

caminho_saida = (diretorio_script / nome_arquivo_saida).resolve()

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
        tamanho_total = 0

        for f in arquivos:
            caminho = raiz / f
            tamanho = os.path.getsize(caminho)
            tamanho_total += tamanho
        
        pagina.write(f"<p>Diretório: {raiz} | Tamanho: {tamanho_total} bytes</p>\n")

    pagina.write("</body>\n")
    pagina.write("</html>\n")