# Exercício 4.1: Analise o Programa 4.1. Responda o que acontece se o primeiro e o segundo valor forem iguais? Explique

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

if a > b:
    print('O primeiro valor é o maior.')
if b > a:
    print('O segundo valor é o maior.')

# R: Não acontece nada, pois não vai entrar em nenhuma das duas condições.