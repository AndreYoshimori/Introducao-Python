# Exercício 5.15: Escreva um programa para controlar uma pequena máquina registradora. 
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de código a seguir para obter o preço de cada produto.
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".

total = 0

while True:
    codigo = input('Digite o código do produto ou 0 para finalizar: ')
    while not codigo.isnumeric():
            codigo = input('Digite o código do produto ou 0 para finalizar: ')
    codigo = int(codigo)

    if codigo == 0:
        break
    elif codigo != 1 and codigo != 2 and codigo != 3 and codigo != 5 and codigo != 9:
        print('Código inválido')        
    else:
        quantidade = input('Digite a quantidade comprada: ')
        while not quantidade.isnumeric():
            quantidade = input('Digite a quantidade comprada: ')
        quantidade = int(quantidade)

        if codigo == 1:
            preco = 0.5
        elif codigo == 2:
            preco = 1
        elif codigo == 3:
            preco = 4
        elif codigo == 5:
            preco = 7
        else:
            preco = 8
        total += quantidade * preco

print(f'Valor total: R$ {total:.2f}')