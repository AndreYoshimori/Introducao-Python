# Exercício 6.7: Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. Exemplo:
# (()) OK
# ()()(()()) OK
# ()) Erro
# Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilha-lá a cada fecha parênteses.
# Ao desempilhar, verifique se o topo da pilha é um abre parênteses.
# Se a expressão estiver correta, sua pilha estará vazia no final.

parenteses = False

while not parenteses:
    expressao = input('Digite a expressão de parênteses: ')
    parenteses = True
         
    x = 0   
    while x < len(expressao):
        if expressao[x] != '(' and expressao[x] != ')':
            parenteses = False
            print('Expressão inválida. Digite apenas parênteses.')
            break
        x += 1
        
pilha = []

x = 0
while x < len(expressao):
    if expressao[x] == '(':
        pilha.append('(')
    else:
        if len(pilha) > 0:
            del pilha[0]
        else:
            print('Ordem incorreta dos parênteses.')
            break
    x += 1
else:
    if len(pilha) > 0:
        print('Ordem incorreta dos parênteses.')
    else:
        print('Ordem correta dos parênteses.')
        