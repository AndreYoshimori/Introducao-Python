# Exercício 9.40: Modifique o programa visualiza.py para imprimir apenas os 512 primeiros bytes do arquivo.

import sys
import itertools


def imprime_bytes(imagem, bytes_por_linha=16):
    for b in itertools.batched(imagem, bytes_por_linha):
        hex_view = " ".join([f"{v:02x}" for v in b])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
        print(f"{hex_view} {" " * 3 * (bytes_por_linha - len(b))}{tview}")

if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        imagem = f.read(512)

imprime_bytes(imagem)
