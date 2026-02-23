# Exercício 12.2: Reescreva a função que mostra os números na entrada ABC431DEF901c431203FXEW9, mas usando a função verifica_padrao.

entrada = "ABC431DEF901c431203FXEW9"

def verifica_padrao(entrada, padroes):
    posicao = 0
    
    for padrao in padroes:
        achou, _, fim = padrao(entrada[posicao:])
        if achou > 0:
            posicao += fim + 1
        else:
            return -1, -1, -1
        
    return 1, 0, posicao - 1


def numeros(entrada):
    posicao = 0

    for caractere in entrada:
        if "0" <= caractere <= "9":
            posicao += 1
        else:
            break
    
    if posicao > 0:
        return 1, 0, posicao - 1
    return -1, -1, -1
        
i = 0
while i < len(entrada):
    achou, inicio, fim = verifica_padrao(entrada[i:], [numeros])
    if achou > 0:
        print(f"Número encontrado nas posições: {i+inicio} a {i+fim}")
        print(f"{entrada[i + inicio : i + fim + 1]}\n")
        i += fim + 1
    else:
        i += 1
