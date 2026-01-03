# Exercício 8.22: Modifique o programa da calculadora que usa partial para suportar mais duas operações: raiz para raiz quadrada e potência para exponenciação.

import operator
import math
from functools import partial


def executa_binaria(operacao, simbolo, operando1, operando2):
    resultado = operacao(float(operando1), float(operando2))
    print(f'{operando1} {simbolo} {operando2} = {resultado}')


def executa_unaria(operacao, simbolo, operando):
    resultado = operacao(float(operando))
    print(f'{simbolo}{operando} = {resultado}')

operacoes = {
    "+": partial(executa_binaria, operator.add, "+"),
    "-": partial(executa_binaria, operator.sub, "-"),
    "*": partial(executa_binaria, operator.mul, "x"),
    "/": partial(executa_binaria, operator.truediv, "/"),
    "potencia": partial(executa_binaria, operator.pow, "^"),
    "raiz": partial(executa_unaria, math.sqrt, "√"),
}

operacao = input("Operação (+, -, *, /, potencia, raiz): ").strip().lower()

if operacao not in operacoes:
    print("Operação inválida.")
else:
    if operacao == "raiz":
        operando = input("Operando: ")
        operacoes[operacao](operando)
    else:
        operando1 = input("Operando 1: ")
        operando2 = input("Operando 2: ")
        operacoes[operacao](operando1, operando2)
