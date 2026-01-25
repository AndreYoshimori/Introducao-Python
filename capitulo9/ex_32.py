# Exercício 9.32: Modifique o Programa 9.9 de forma a receber o nome do arquivo ou diretório a verificar pela linha de comando.
# Imprima se existir e se for um arquivo ou diretório.

import os
import os.path
import sys


arquivo = sys.argv[1]

if os.path.exists(arquivo):
    if os.path.isdir(arquivo):
        print(f"{arquivo} existe e é um diretório.")
    else:
        print(f"{arquivo} existe e é um arquivo.")
else:
    print(f"{arquivo} não existe.")
