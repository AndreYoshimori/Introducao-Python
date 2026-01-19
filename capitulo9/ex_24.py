# Exercício 9.24: O que acontece com a agenda se ocorrer um erro de leitura ou gravação? Explique.

'''
R: Erros de leitura ou gravação podem ocorrer por arquivo inexistente, problemas de permissão ou falhas de I/O. 
Como o programa não trata exceções, ele pode ser interrompido no meio da operação, deixando a agenda sem ser carregada ou sem ser salva corretamente.
'''