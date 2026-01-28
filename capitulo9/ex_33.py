# Exercício 9.33: Crie um programa que gere uma página HTML com links para todos os arquivos jpg e png 
# encontrados a partir de um diretório informado na lihna de comando.

import os
import os.path
import sys


def pega_extensao(nome):
    extensao = ""
    ponto = False

    for i in range(len(nome)):
        if nome[i] == ".":
            ponto = True
        if ponto:
            extensao += nome[i]
            
    return extensao


def filtra_imagem(nome):
    extensao = pega_extensao(nome)

    if extensao == ".jpg" or extensao == ".jpeg" or extensao == ".png":
        return True

caminho_entrada = sys.argv[1]

if not os.path.exists(caminho_entrada):
    print("Esse diretório não existe.")
else:
    if os.path.isfile(caminho_entrada):
        print("O caminho passado se trata de um arquivo.")
    else:
        lista_arquivos = os.listdir(caminho_entrada)

        lista_imagens = [
            nome 
            for nome in lista_arquivos
            if filtra_imagem(nome)
            ]
        
        with open("capitulo9/imagens.html", "w", encoding="utf-8") as pagina:
            pagina.write("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Imagens</title>
</head>
<body>
""")
            
            for i in range(len(lista_imagens)):
                pagina.write(f'<a href="imagens/{lista_imagens[i]}">Imagem {i}</a>\n')

            pagina.write("</body>\n")
            pagina.write("</html>\n")