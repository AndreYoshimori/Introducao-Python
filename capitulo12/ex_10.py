# Exercício 12.10: Escreva uma função que aceite preços em reais.
# O programa deve ignorar espaços em branco e aceitar valores prefixados com R$ ou não(com r ou R).
# O usuário deve entrar valores corretamente formatados com o ponto separando os milhares e a vírgulo, os centavos.
# Se o usuário digitar centavos, estes devem ter dois dígitos.

"""
Valores válidos:
R$500
   R$500
R$500,10
R$7.312,10

Valores inválidos:
R$500,1
R$7312.10
"""

# A função deve retornar o valor digitado convertido para float ou gerar uma exceção do tipo ValueError caso o valor entrado seja inválido.