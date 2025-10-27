# Exercício 2: Traga ao usuário todas as informações sobre um carro da sua escolha:
carros = {'nome': ['celta', 'up', 'kombi', 'uno'],
          'número de portas': [4, 2, 6, 2],
          'preço': [1000, 200, 300, 100],
          'ano de fabricação': [2014, 2018, 1970, 2005]}

def encontra_indice(nome_carro):
    for i in range(len(carros['nome'])):
        if carros['nome'][i] == nome_carro:
            return i
    else:
        print('Carro não encontrado.')
        return None

def mostrar_informacoes():
    print(carros['nome'])
    nome_carro = input('Digite o nome do carro que você deseja ver as informações: ').strip().lower()
    i = encontra_indice(nome_carro)
    if i is None:
        return
    print(f'Informações do {nome_carro.title()}')
    for chave in carros:
        chave_formatada = chave.title()
        print(f'{chave_formatada}: {str(carros[chave][i]).title()}')

def main():
    mostrar_informacoes()

main()