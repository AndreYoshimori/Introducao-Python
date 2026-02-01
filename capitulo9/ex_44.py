# Exercício 9.44: Modifique o programa anterior para receber um terceiro parâmetro com a tabela de conversão de cores no formato JSON.

import sys
import json
from pathlib import Path


def bytes_little_endian(numero, nbytes=4, sinal=False):
    return int(numero).to_bytes(nbytes, "little", signed=sinal)


def padding(valor, tamanho=4):
    resto = valor % tamanho
    return valor if resto == 0 else valor + (tamanho - resto)


def ler_desenho(caminho):
    linhas = Path(caminho).read_text(encoding="utf-8").splitlines()
    if not linhas:
        raise ValueError("Arquivo de desenho vazio.")

    largura = len(linhas[0])
    for i, linha in enumerate(linhas):
        if len(linha) != largura:
            raise ValueError(f"Linhas devem ter o mesmo tamanho. Linha {i} está diferente.")
    return linhas


def ler_cores_json(caminho):
    data = json.loads(Path(caminho).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("JSON de cores deve ser um objeto (dicionário).")

    tabela = {}
    for chave, valor in data.items():
        if not isinstance(chave, str) or len(chave) != 1:
            raise ValueError(f"Chave inválida (1 caractere): {chave!r}")
        if (
            not isinstance(valor, (list, tuple))
            or len(valor) != 3
            or not all(isinstance(x, int) for x in valor)
        ):
            raise ValueError(f"Valor inválido para {chave!r}. Use [R, G, B] com inteiros.")
        r, g, b = valor
        if not all(0 <= x <= 255 for x in (r, g, b)):
            raise ValueError(f"RGB fora de 0..255 para {chave!r}: {valor}")
        tabela[chave] = (r, g, b)

    return tabela


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

    linhas_bytes = []
    for linha in desenho_expandido:
        linha_bin = []
        for ch in linha:
            if ch not in letra_para_cor:
                raise KeyError(f"Caractere {ch!r} não existe na tabela de cores.")
            r, g, b = letra_para_cor[ch]
            linha_bin.append(bytes([b, g, r]))  # BMP 24-bit = BGR
        linhas_bytes.append(b"".join(linha_bin))

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
        bytes_little_endian(-altura, sinal=True),
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
    if len(sys.argv) != 4:
        print("Uso: python ex_9_44.py <saida.bmp> <desenho.txt> <cores.json>")
        sys.exit(1)

    saida = sys.argv[1]
    arquivo_desenho = sys.argv[2]
    arquivo_cores = sys.argv[3]

    desenho = ler_desenho(arquivo_desenho)
    letra_para_cor = ler_cores_json(arquivo_cores)

    multiplicador = 32
    desenho_expandido = expandir_desenho(desenho, multiplicador)
    gerar_bmp_24bits(saida, desenho_expandido, letra_para_cor)


if __name__ == "__main__":
    main()
