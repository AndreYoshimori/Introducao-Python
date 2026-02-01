# Exercício 9.42: Modifique o Programa 9.20 para que receba o nome da imagem a gerar pela linha de comando.

import sys
from pathlib import Path


ARQUIVO_PADRAO = "dados/imagem_python.bmp"


def bytes_little_endian(numero, nbytes=4, sinal=False):
    return int(numero).to_bytes(nbytes, "little", signed=sinal)


def padding(valor, tamanho=4):
    resto = valor % tamanho
    return valor if resto == 0 else valor + (tamanho - resto)


letra_para_cor = {
    " ": (0, 0, 0),      # preto
    "r": (255, 0, 0),    # vermelho
    "g": (0, 255, 0),    # verde
    "b": (0, 0, 255),    # azul
}


desenho = [
    " rrrr r r bbbbb b   b  ggggg   g   g  r",
    " r  r r r   b   b   b  g   g  gg   g  r",
    " r  r r r   b   b   b  g r r g  g g  g  r",
    " rrr  r     b  bbbbbb  g   g  g g  g  r",
    " r    r     b   b   b  gr b rg  g  gg    ",
    " r    r     b   b   b  g rrr g  g   gg  r",
    " r    r     b   b   b  ggggg   g   g  r",
]


def checa_largura(desenho):
    largura = len(desenho[0])
    for i, linha in enumerate(desenho):
        if len(linha) != largura:
            raise ValueError(f"Linhas devem ter o mesmo tamanho. Linha {i} está diferente.")
    return largura


def expandir_desenho(desenho, multiplicador):
    expandido = []
    for linha in desenho:
        linha_h = "".join(ch * multiplicador for ch in linha)
        for _ in range(multiplicador):
            expandido.append(linha_h)
    return expandido


def gerar_bmp_24bits(caminho_saida, desenho_expandido, letra_para_cor):
    largura = len(desenho_expandido[0])
    altura = len(desenho_expandido)

    # Converte para bytes (BMP 24-bit usa BGR)
    linhas_bytes = []
    for linha in desenho_expandido:
        linha_bin = []
        for ch in linha:
            r, g, b = letra_para_cor[ch]
            linha_bin.append(bytes([b, g, r]))  # BGR
        linhas_bytes.append(b"".join(linha_bin))

    # Padding por linha (múltiplo de 4 bytes)
    largura_bytes = largura * 3
    largura_com_padding = padding(largura_bytes, 4)
    if largura_com_padding != largura_bytes:
        pad = bytes(largura_com_padding - largura_bytes)
        linhas_bytes = [lb + pad for lb in linhas_bytes]

    tamanho_dados = largura_com_padding * altura

    cabecalho_bmp = b"".join([
        b"BM",
        bytes_little_endian(54 + tamanho_dados),
        bytes(4),
        bytes_little_endian(54),
    ])

    cabecalho_dib = b"".join([
        bytes_little_endian(40),
        bytes_little_endian(largura),
        bytes_little_endian(-altura, sinal=True),  # top-down
        bytes_little_endian(1, 2),
        bytes_little_endian(24, 2),
        bytes_little_endian(0),
        bytes_little_endian(tamanho_dados),
        bytes_little_endian(2835),
        bytes_little_endian(2835),
        bytes_little_endian(0),
        bytes_little_endian(0),
    ])

    dados = b"".join(linhas_bytes)

    assert len(cabecalho_bmp) == 14
    assert len(cabecalho_dib) == 40
    assert len(dados) == tamanho_dados

    Path(caminho_saida).parent.mkdir(parents=True, exist_ok=True)
    with open(caminho_saida, "wb") as f:
        f.write(cabecalho_bmp)
        f.write(cabecalho_dib)
        f.write(dados)

    print(f"Arquivo {caminho_saida} gerado. largura={largura} altura={altura} bytes={tamanho_dados}")


def main():
    saida = sys.argv[1] if len(sys.argv) > 1 else ARQUIVO_PADRAO

    checa_largura(desenho)
    multiplicador = 32
    desenho_expandido = expandir_desenho(desenho, multiplicador)
    gerar_bmp_24bits(saida, desenho_expandido, letra_para_cor)


if __name__ == "__main__":
    main()
