# Exercício 4.12: Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunta a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
# Calcule o preço de acordo com a tabela a seguir(tabela no livro).

energia = float(input('Digite a quantidade de kWh consumidade: '))
instalacao = input('Qual o seu tipo de instalação? R: residência  I: indústria  C: comércio')

preco = None

if instalacao == 'R':
    if energia <= 500:
        preco = energia * 0.40
    else:
        preco = energia * 0.65
elif instalacao == 'C':
    if energia <= 1000:
        preco = energia * 0.55
    else:
        preco = energia * 0.60
elif instalacao == 'I':
    if energia <= 5000:
        preco = energia * 0.55
    else:
        preco = energia * 0.60
else: 
    print('Instalação não identificada.')
    
if preco is not None:
    print(f'Preço a pagar: R$ {preco}')