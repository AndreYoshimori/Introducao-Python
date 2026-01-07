# Programa 9.5: Processamento de um arquivo

largura = 79

with open("dados/entrada.txt", "r") as entrada:
    for linha in entrada:
        linha = linha.rstrip("\n")
        if linha[0] == ";":
            continue
        elif linha[0] == ">":
            print(linha[1:].rjust(largura))
        elif linha[0] == "*":
            print(linha[1:].center(largura))
        else:
            print(linha)
            