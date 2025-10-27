# Exercício 3.11: Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar.
preco = float(input('Digite o preço da mercadoria: '))
desconto = float(input('Digite a porcentagem do desconto: '))
valor_desconto = desconto / 100 * preco
preco_descontado = preco - valor_desconto
print(f'O valor do desconto é de R$ {valor_desconto}, e o preço a pagar são R$ {preco_descontado}.')