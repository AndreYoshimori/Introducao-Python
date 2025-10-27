# Exercício 3: Use o dicionário do item anterior para trazer todas as informações sobre o carro mais caro.
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

def escolhe_carro():
    print(carros['nome'])
    nome_carro = input('Digite o nome do carro que você deseja ver as informações: ').strip().lower()
    i = encontra_indice(nome_carro)
    if i is None:
        return
    mostra_informacoes(i)
    
def mostra_informacoes(i):
    for chave in carros:
        chave_formatada = chave.title()
        print(f'{chave_formatada}: {str(carros[chave][i]).title()}')
        
def encontra_indice_mais_caro():
    indice_mais_caro = 0
    for i in range(len(carros['preço'])):
        if carros['preço'][i] > carros['preço'][indice_mais_caro]:
            indice_mais_caro = i
    mostra_informacoes(indice_mais_caro)

def main():
    encontra_indice_mais_caro()

main()