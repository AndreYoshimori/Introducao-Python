# Programa 9.13: Árvore de diretórios sendo percorrida - com pathlib

import sys
from pathlib import Path


for raiz, diretorios, arquivos in Path(sys.argv[1]).walk():
    print(f"Caminho: {raiz}")

    for d in diretorios:
        print(f"  {d}/")

    for f in arquivos:
        print(f"  {f}")
    
    print(f"{len(diretorios)} diretório(s), {len(arquivos)} arquivo(s)")
    