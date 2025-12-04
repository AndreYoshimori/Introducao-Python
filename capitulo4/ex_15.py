# Exercício 4.15: Reescreva o programa a seguir com if-elif-else.

'''
hora = int(input('Digite a hora atual:'))
if hora < 12:
    print('Bom dia!')
if hora >= 12 and hora <= 18:
    print('Boa tarde!')
if hora >= 18:
    print('Boa noite!')
'''

hora = input('Digite a hora atual: ')
while not hora.isnumeric():
    hora = input('Digite a hora atual: ')
hora = int(hora)

if hora < 12:
    print('Bom dia!')
elif hora >= 12 and hora <= 18:
    print('Boa tarde!')
else:
    print('Boa noite!')