# Exercício 8.20: Escreva um generator capaz de gerar uma sequência com o fatorial de 1 até n, em que n é passado como parâmetro para o gerador.

def gera_fatorial(fim):
    fatorial = 1
    num = 1
    while num <= fim:
        fatorial *= num
        yield fatorial
        num += 1

for fatorial in gera_fatorial(5):
    print(fatorial)