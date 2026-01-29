# Programa 9.41: Altere o programa visualiza.py para receber o número máximo de 
# bytes a imprimir e quantos bytes por linha pela linha de comando.

import sys
import itertools


def imprime_bytes(imagem, bytes_por_linha=16):
    for b in itertools.batched(imagem, bytes_por_linha):
        hex_view = " ".join([f"{v:02x}" for v in b])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
        print(f"{hex_view} {" " * 3 * (bytes_por_linha - len(b))}{tview}")

if __name__ == "__main__":
    bytes_por_linha = int(sys.argv[2])
    max_bytes = int(sys.argv[3])

    with open(sys.argv[1], "rb") as f:
        imagem = f.read(max_bytes)

imprime_bytes(imagem, bytes_por_linha)