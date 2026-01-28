# Programa 9.12: Árvore de diretórios sendo percorrida

import os
import sys


for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print(f"Caminho: {raiz}")

    for d in diretorios:
        print(f"  {d}/")

    for f in arquivos:
        print(f"  {f}")
    
print(f"{len(diretorios)} diretório(s), {len(arquivos)} arquivo(s)")