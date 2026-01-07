# Exercício 8: Escreva um código capaz de alterar números por extenso numa frase pelos caracteres correspondentes.
# Exemplo: Eu tenho uma aula na cinco zero dois -> Eu tenho uma aula na 502

numeros = {
    'zero': '0',
    'dois': '2',
    'cinco': '5'
}

frase = 'Eu tenho uma aula na cinco zero dois'

for key in numeros.keys():
    frase = frase.replace(key+' ',numeros[key])
    frase = frase.replace(key, numeros[key])
    
print(frase)
