# Programa 9.19: Criando uma imagem em formato binário

imagem_em_hexa = """
42 4d
46 00 00 00
00 00
00 00
36 00 00 00
28 00 00 00
02 00 00 00
02 00 00 00
01 00
18 00
00 00 00 00
10 00 00 00
13 0b 00 00
13 0b 00 00
00 00 00 00
00 00 00 00
00 00 FF
FF FF FF
00 00
FF 00 00
00 FF 00
00 00
"""

imagem_bytes = bytes.fromhex(imagem_em_hexa)

with open("dados/imagem.bmp", "wb") as f:
    f.write(imagem_bytes)
    