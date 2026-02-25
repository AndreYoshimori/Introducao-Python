# Exercício 12.5: Crie uma função sequencias que recebe qmax e qmin.
# Ela deve funcionar de forma semelhante a numero, mas chamando a função sequencia.
# Ela deve também funcionar quando qmin é 0, ou seja, quando a sequência é opcional.

entrada = "abcd()()()ef()(())gh()()"

def sequencia(entrada, padrao):
    posicao, posicao_max = 0, len(padrao)

    for caractere in entrada:
        if caractere == padrao[posicao]:
            posicao += 1
        else:
            break

        if posicao == posicao_max:
            return 1, 0, posicao -1
        
    return -1, -1, -1


def sequencias(entrada, padrao, qmin, qmax):
    num = 0

    i = 0
    while i < len(entrada):
        achou, _, _ = sequencia(entrada[i:], padrao)
        if achou > 0:
            num += 1
            i += len(padrao)
        else:
            break

    if qmin <= num <= qmax:
        return num, 0, num * len(padrao) - 1
    else:
        return -1, -1, -1

posicao = 0
while posicao < (len(entrada)):
    achou, inicio, fim = sequencias(entrada[posicao:], padrao="()", qmin = 0, qmax=3)
    if achou > 0:
        print(f"Valor encontrado nas posições: {posicao+inicio} a {posicao+fim}")
        print(entrada[posicao + inicio : posicao + fim + 1])
        posicao += fim + 1
    else:
        posicao += 1
