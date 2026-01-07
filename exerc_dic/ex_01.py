# Exercício 1: Modifique o seguinte código para eliminar o uso de condicionais.

resp = input('Diga oi ou tchau: ').strip().lower()

comprimento = {'oi': 'Olá!',
               'tchau': 'Até logo!'}

print(comprimento.get(resp, 'Não entendi'))
