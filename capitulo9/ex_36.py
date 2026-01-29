# Exercício 9.36: Utilizando a função os.walk, crie um programa que calcule o espaço 
# ocupado por diretório e subdiretório, gerando uma página HTML com os resultados.

import sys
from pathlib import Path
import os.path
import os


caminho_entrada = Path(sys.argv[1]).resolve()

diretorio_script = Path(sys.argv[0]).parent.resolve()
nome_arquivo_saida = "tamanho_diretorios.html"

caminho_saida = diretorio_script / nome_arquivo_saida

def calcula_tamanho(raiz):
    tamanho_total = 0

    diretorios = []
    arquivos = []

    lista_elementos = os.listdir(raiz)

    for e in lista_elementos:
        if os.path.isdir(raiz / e):
            diretorios.append(e)
        else:
            arquivos.append(e)

    for d in diretorios:
        tamanho_d = calcula_tamanho(raiz / d)
        tamanho_total += tamanho_d
    
    for f in arquivos:
        tamanho_f = os.path.getsize(raiz / f)
        tamanho_total += tamanho_f

    pagina.write(f"<p>Diretório: {raiz} | Tamanho: {tamanho_total} bytes</p>\n")

    return tamanho_total

with caminho_saida.open("w", encoding="utf-8") as pagina:
    pagina.write("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Imagens</title>
</head>
<body>
""")

    calcula_tamanho(caminho_entrada)

    pagina.write("</body>\n")
    pagina.write("</html>\n")

# Nesse exercício eu preferi usar uma função recursiva ao invés do os.walk para deixar o cálculo explícito e entender melhor a estrutura.