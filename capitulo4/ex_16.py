# Exercício 4.16: Corrija o programa a seguir:

'''
media = input('Digite sua média.')
if media < 4:
    print('Infelizmente você reprovou.')
if media < 7:
    print('Você ficou de recuperação.')
if media > 7:
    print('Você passou de ano.')
'''

media = input('Digite sua média: ')
while not media.isnumeric():
    media = input('Digite sua média: ')
media = int(media)

if media < 4:
    print('Infelizmente você reprovou.')
elif media < 7:
    print('Você ficou de recuperação.')
else:
    print('Você passou de ano.')