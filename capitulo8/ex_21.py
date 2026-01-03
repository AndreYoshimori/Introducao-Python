# Exercício 8.21: Escreva uma função que gere os números como a função range do Python.
# Essa função recebe três parâmetros e seu comportamento muda se passarmos um, dois ou três parâmetros.
# Chame-a de faixa
'''
Exemplos:
list(faixa(1))
[0, 1]
list(faixa(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(faixa(0, 10, 2))
[0, 2, 4, 6, 8, 10]
'''
# Você deve ter percebido que, diferente de range, a função faixa considera o fim do interevalo fechado, ou seja, o último número faz parte da faixa.

def faixa(parametro1, parametro2 = None, parametro3 = None):
    inicio = 0
    fim = parametro1
    intervalo = 1
    
    if parametro2 is not None:
        inicio = parametro1
        fim = parametro2
    if parametro3 is not None:
        intervalo = parametro3

    num = inicio
    while num <= fim:
        yield num
        num += intervalo

for n in faixa(0, 40, 5):
    print(n)