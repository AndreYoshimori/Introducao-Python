# Exercício 8.11: Escreva uma função para validar uma variável string.
# Essa função recebe como parâmetro a string, o número mínimo e máimo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimos, e falso, caso contrário.

def valida_string(string, minimo, maximo):
    if len(string) < minimo or len(string) > maximo:
        return False
    return True

palavra = input('Digite uma palavra: ')

if valida_string(palavra, 4, 10):
    print('Palavra válida.')
else:
    print('Palavra inválida.')