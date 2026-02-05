# Exercício 10.9: Modifique o método resumo da classe Conta para exibir o nome e o telefone de cada cliente.

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print("Clientes da conta:")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome} | Telefone {cliente.telefone}")
        print(f"\nCC Número: {self.numero} Saldo: {self.saldo:10.2f}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo Insuficiente para realizar o saque.")
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")

        for operacao in self.operacoes:
            print(f"{operacao[0]:10s} {operacao[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:10.2f}\n")

    
joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta = Conta([joao, maria], 1, 500)

conta.resumo()
