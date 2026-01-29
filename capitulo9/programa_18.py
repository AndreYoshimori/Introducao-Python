# Programa 9.18: Visualizador de arquivo em formato binário

import sys
import itertools


def imprime_bytes(imagem, bytes_por_linha=16):
    for b in itertools.batched(imagem, bytes_por_linha):
        hex_view = " ".join([f"{v:02x}" for v in b])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
        print(f"{hex_view} {" " * 3 * (bytes_por_linha - len(b))}{tview}")

if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        imagem = f.read()

imprime_bytes(imagem)
