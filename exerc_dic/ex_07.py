# Exercício 7: Escreva um código capaz de contar a quantidade de vezes que uma palavra aparece numa frase, por exemplo:
# "O bispo de Constantinopla é um bom desconstantinopolitanizador, quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será."

frase = 'O bispo de Constantinopla é um bom desconstantinopolitanizador, quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será.'
frase = frase.lower()
frase = frase.replace(',', '').replace('.', '')

lista_palavras = frase.split()

contagem = {}

for palavra in lista_palavras:
    #contagem[palavra] = contagem.get(palavra, 0) + 1
    if palavra not in contagem:
        contagem[palavra] = 0
    contagem[palavra] += 1

print(contagem)