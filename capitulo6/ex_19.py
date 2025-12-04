# Exercício 6.19: Altere o Programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida.
# Verifique se o nome do produto digitado existe no dicionário e só então efetue a baixa em estoque.

estoque = {'tomate': [1000, 2.30],
           'alface': [500, 0.45],
           'batata': [2001, 1.20],
           'feijão': [100, 1.50]}
venda = []

total = 0

while True:
    nome_produto = input('Digite o nome do produto ou 0 para finalizar: ')
    if nome_produto == '0':
        break
    elif not nome_produto in estoque:
        print('Produto não identificado')
    else:
        quantidade_vendida = input(f'Digite a quantidade vendida de {nome_produto}: ')
        while not quantidade_vendida.isnumeric():
            quantidade_vendida = input(f'Por favor, insira apenas números. Digite a quantidade vendida de {nome_produto}: ')
        quantidade_vendida = int(quantidade_vendida)
        venda.append([nome_produto, quantidade_vendida])

print('Vendas:')
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto}: {quantidade} x {preco:.2f} = {custo:.2f}')
    estoque[produto][0] -= quantidade
    total += custo
        
print(f'Custo total: {total:.2f}\n')

print('Estoque:\n')
for chave, dados in estoque.items():
    print(f'Descrição: {chave}')
    print(f'Quantidade: {dados[0]}')
    print(f'Preço: {dados[1]:.2f}\n')