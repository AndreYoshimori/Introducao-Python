# Exercício 9.31: Crie um programa que corrija o Programa 9.9 de forma a verificar se z existe e é um diretório.

import os
import os.path


if os.path.exists("z"):
    if os.path.isdir("z"):
        print("z existe e é um diretório.")
    else:
        print("z existe e é um arquivo.")
else:
    print("z não existe.")
