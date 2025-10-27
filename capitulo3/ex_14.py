# Exercício 3.14: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
dias = int(input('Digite por quantos dias o carro foi alugado: '))
km_rodados = int(input(f'Digite quantos km foram rodados nesses {dias} dias: '))
preco = dias * 60 + km_rodados * 0.15
print(f'O preço a ser pago é de R$ {preco}.')