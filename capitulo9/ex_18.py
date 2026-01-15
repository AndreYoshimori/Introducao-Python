# Exercício 9.18: O que acontece se nome ou telefone contiverem o caractere usado como separador em seus conteúdos? 
# Explique o problema e proponha uma solução.

'''
R: Se o nome ou o telefone contiverem o caractere separador(#), a leitura do arquivo será feita de forma incorreta, pois o método split("#")
irá dividir a linha em mais partes que o esperado. Com isso, os dados não serão separados corretamente e o contato será carregado de forma
errada na agenda.
Uma possível solução para essa situação é validar as entradas do usuário, de modo a impedir o uso do caractere separador.
'''