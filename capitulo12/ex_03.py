# Exercício 12.3: Utilizando a função verifica_padrao, escreva uma função que detecte uma data 
# no formato dd/mm/aa em que dd é o dia, mm o mês e aa o ano.
# A função deve apenas detectar o padrão da data e não precisa verificar se a data é válida.

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


def data(entrada):
    return verifica_padrao(
        entrada, 
        [partial(numero, qmin=2, qmax=2),
         partial(sequencia, padrao="/"),
         partial(numero, qmin=2, qmax=2),
         partial(sequencia, padrao="/"),
         partial(numero, qmin=2, qmax=4)]
    )

for posicao in range(len(entrada)):
    achou, inicio, fim = data(entrada[posicao:])
    if achou > 0:
        print(f"Data encontrada nas posições: {posicao+inicio} a {posicao+fim}")
        print(entrada[posicao + inicio : posicao + fim + 1])
