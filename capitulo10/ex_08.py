# Exercício 10.8: Altere o programa de forma que a mensagem saldo insuficiente seja exibida 
# caso haja tentativa de sacar mais dinheiro que o saldo disponível.

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
        print(f"CC Número: {self.numero} Saldo: {self.saldo:10.2f}")

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

maria = Cliente("Maria da Silva", "555-4321")
conta = Conta([maria], 1, 100)

conta.resumo()
conta.saque(200)
