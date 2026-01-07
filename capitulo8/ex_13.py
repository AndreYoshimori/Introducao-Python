# Exercício 8.13: Escreva uma função que receba uma string com as opções válidas a aceitar (cada opção é uma letra).
# Converta as opções válidas para letras minúsculas.
# Utilize input para ler uma opção, converter o valor para letras minúsculas e verificar se a opção é válida.
# Em caso de opção inválida, a função deve pedir ao usuário que digite novamente outra opção.

def opcoes_validas(opcoes):
    opcoes = opcoes.lower()

    while True:
        opcao = input('Digite uma opção: ').lower()
        if opcao in opcoes:
            print('Opção válida!')
            break
        print('Opção inválida.')

opcoes_validas('abcde')
