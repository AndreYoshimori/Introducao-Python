# Execício 4.11: Escreva um programa para apovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))

anos = input('Digite quantos anos vão ser destinados ao pagamento dessa casa: ')
while not anos.isnumeric():
    anos = input('Digite quantos anos vão ser destinados ao pagamento dessa casa: ')
anos = int(anos)

meses = anos * 12
prest = casa / meses

if prest > (salario * 0.3):
    print(f'A prestação mensal, que é de R$ {prest:.2f} excede 30% do seu salário, que é de R$ {(salario * 0.3):.2f}. Não pode comprar.')
else:
    print(f'Sua prestação mensal vai ser de {prest:.2f}')
    