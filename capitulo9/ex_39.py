# Exercício 9.39: Modifique o Programa 9.6 da agenda.
# Faça-o ler e gravar um arquivo, mas no formato JSON.

import json


agenda = []

def pede_nome():
    return input("Nome: ")


def pede_telefone():
    return input("Telefone: ")


def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")


def pede_nome_arquivo():
    return input("Nome do arquivo: ")


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])


def apaga():
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome não encontrado.")

    
def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")

    
def lista():
    print("\nAgenda\n\n------")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("------\n")


def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = json.load(arquivo)

        
def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(agenda, arquivo, ensure_ascii=False)


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")
            

def menu():
    print("""
  1 - Novo
  2 - Altera
  3 - Apaga
  4-  Lista
  5 - Grava
  6 - Lê
          
  0 - Sai
""")
    
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)

while opcao := menu():
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
        