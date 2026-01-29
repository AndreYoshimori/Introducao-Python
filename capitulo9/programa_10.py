# Programa 9.10: Propriedades de um arquivo

import os
import os.path
import time
import sys


nome = sys.argv[1]

print(f"Nome: {nome}")
print(f"Tamanho: {os.path.getsize(nome)}")
print(f"Criado: {time.ctime(os.path.getctime(nome))}")
print(f"Modificado: {time.ctime(os.path.getmtime(nome))}")
print(f"Acessado: {time.ctime(os.path.getatime(nome))}")
