# Exercício 5: Pergunte ao usuário se ele gostaria de cadastrar um carro novo e implemente esta funcionalidade.

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
        

def encontra_indice_extremo(tipo):
    indice = 0
    for i in range(len(carros['preço'])):
        if tipo == 'maior' and carros['preço'][i] > carros['preço'][indice]:
            indice = i
        elif tipo == 'menor' and carros['preço'][i] < carros['preço'][indice]:
            indice = i
    return indice


def mostra_mais_caro():
    i = encontra_indice_extremo('maior')
    print('Informações do carro mais caro:')
    mostra_informacoes(i)


def mostra_mais_barato():
    i = encontra_indice_extremo('menor')
    print('Informações do carro mais barato:')
    mostra_informacoes(i)


def cadastrar_carro():
    for elem in carros.keys():
        entrada = input(f'Digite o {elem} do carro: ')
        if elem == 'nome':
            carros[elem].append(entrada)
        else:
            carros[elem].append(int(entrada))


def main():
    resp = input('Gostaria de cadastrar um carro(sim)?')
    if resp == 'sim':
        cadastrar_carro()
        print(carros)

main()