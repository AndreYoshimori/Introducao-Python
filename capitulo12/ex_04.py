# Exercício 12.4: Utilizando a função verifica_padrao, escreva uma função que detecte um valor em reais 
# no formato: R$9999,99 em que 9 representa qualquer dígito.
# O primeiro número pode ter um ou mais dígitos, mas a segunda parte (centavos) deve ter no máximo dois dígitos.

from functools import partial


entrada = "Compre por R$50,72. Ligue já (92)5431-2201 antes de 10/12/2033"

def numero(entrada, qmin, qmax):
    num = 0

    for caractere in entrada:
        if caractere.isnumeric():
            num += 1
        else:
            break

    if qmin <= num <= qmax:
        return num, 0, num - 1
    else:
        return -1, -1, -1


def sequencia(entrada, padrao):
    posicao, posicao_max = 0, len(padrao)

    for caractere in entrada:
        if caractere == padrao[posicao]:
            posicao += 1 # Caracteres iguais, testa o próximo caractere
        else:
            break # Saiu da sequência

        if posicao == posicao_max: # Achou toda a sequência
            return 1, 0, posicao -1
        
    return -1, -1, -1


def verifica_padrao(entrada, padroes):
    posicao = 0
    
    for padrao in padroes:
        achou, _, fim = padrao(entrada[posicao:])
        if achou > 0:
            posicao += fim + 1
        else:
            return -1, -1, -1
        
    return 1, 0, posicao - 1


def valor(entrada):
    return verifica_padrao(
        entrada,
        [partial(sequencia, padrao="R$"),
         partial(numero, qmin=1, qmax=len(entrada)),
         partial(sequencia, padrao=","),
         partial(numero, qmin=2, qmax=2)]
    )

for posicao in range(len(entrada)):
    achou, inicio, fim = valor(entrada[posicao:])
    if achou > 0:
        print(f"Valor encontrado nas posições: {posicao+inicio} a {posicao+fim}")
        print(entrada[posicao + inicio : posicao + fim + 1])
