# Exercício 9.15: Altere o Programa 7.2, o jogo da forca.
# Utilize um arquivo em que uma palavra seja gravada a cada linha.
# Use um editor de textos para gerar o arquivo.
# Ao iniciar o programa, utilize esse arquivo para carregar (ler) a lista de palavras.
# Experimente também perguntar o nome do jogador e gerar um arquivo com o número de acertos dos cinco melhores.

from pathlib import Path
import random


diretorio = Path("dados")
caminho_entrada = diretorio / "palavras.txt"
caminho_saida = diretorio / "ranking.txt"

with caminho_entrada.open("r") as entrada:
    lista_palavras = entrada.readlines()
    numero_palavras = len(lista_palavras)

    while len(lista_palavras) > 0:
        venceu = False
        indice = random.randint(0, len(lista_palavras) - 1)
        palavra = lista_palavras[indice]

        for x in range(20):
            print()

        digitadas = []
        acertos = []
        erros = 0

        linha1 = list('X==:==')
        linha2 = list('X  :  ')
        linha3 = list('X     ')
        linha4 = list('X     ')
        linha5 = list('X     ')
        linha6 = list('X     ')
        linha7 = list('==========')

        desenho_forca = [linha1, linha2, linha3, linha4, linha5, linha6, linha7]

        while True:
            senha = ""

            for letra in palavra:
                senha += letra if letra in acertos else "-"
                
            print(senha)

            if senha == palavra:
                print('\nVocê acertou')
                venceu = True
                break

            tentativa = input('\nDigite uma letra: ').lower().strip()

            if tentativa in digitadas:
                print('Você já tentou essa letra!')
                continue
            else:
                digitadas += tentativa
                if tentativa in palavra:
                    acertos += tentativa
                else:
                    erros += 1
                    print('Você errou')

            if erros == 1:
                linha3[3] = '0'

            elif erros == 2:
                linha4[2] = "\\"

            elif erros == 3:
                linha4[3] = "|"

            elif erros == 4:
                linha4[4] = "/"

            elif erros == 5:
                linha5[2] = "/"

            elif erros == 6:
                linha5[4] = "\\"
            
            for i in range(len(desenho_forca)):
                linha = "".join(desenho_forca[i])
                print(linha)

            if erros == 6:
                print('\nEnforcado')
                print(f'A palavra era {palavra}')
                break
        
        if venceu:
            del lista_palavras[indice]
        else:
            break

with caminho_saida.open("a+") as saida:
    saida.readlines()
