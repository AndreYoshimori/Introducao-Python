# Exercício 5.24: Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

n = input('Informe quantos números primos você deseja ver em ordem crescente: ')
while not n.isnumeric():
    n = input('Informe quantos números primos você deseja ver em ordem crescente: ')
n = int(n)

cont = 0
num = 2

while cont < n:
    if num == 2:
        print(2)
        cont += 1
    else:
        primo = True
        i = 2
        while i < num:
            if num % i == 0:
                primo = False
                break
            else:
                i += 1
        if primo:
            print(num)
            cont += 1
    num += 1
    