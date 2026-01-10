# Exercício 9.6: Modifique o Programa 9.5 para imprimir 40 vezes o símbolo de = se este for o primeiro caractere da linha.
# Adicione também a opção para parar de imprimir até que se pressione a tecla Enter cada vez que uma linha iniciar com . (ponto) como primeiro caractere.

from pathlib import Path


caminho_entrada = Path("dados") / "entrada.txt"

largura = 79

with caminho_entrada.open("r", encoding="utf-8") as entrada:
    for linha in entrada:
        linha = linha.rstrip("\n")
        if linha[0] == ";":
            continue
        elif linha[0] == ">":
            print(linha[1:].rjust(largura))
        elif linha[0] == "*":
            print(linha[1:].center(largura))
        elif linha[0] == "=":
            print("=" * 40)
        elif linha[0] == ".":
            input('Tecle Enter para continuar a imprimir: ')
        else:
            print(linha)
            