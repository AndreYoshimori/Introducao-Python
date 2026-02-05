# Exercício 10.13: Altere a classe ContaEspecial de forma que seu extrato exiba o limite e o total disponível para saque.

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
        print(f"CC Número: {self.numero} Saldo: {self.saldo:10.2f}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            return False
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")

        for operacao in self.operacoes:
            print(f"{operacao[0]:10s} {operacao[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite
    
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            return False
    
    def extrato(self):
        super().extrato()
        print(f"Limite: {self.limite}")
        print(f"Total disponível para saque: {self.limite + self.saldo}")


maria = Cliente("Maria da Silva", "555-4321")

conta_especial = ContaEspecial([maria], numero="E-001", saldo=100, limite=200)

conta_especial.deposito(50)
conta_especial.saque(180)
conta_especial.extrato()

conta_especial.saque(200)
conta_especial.extrato()
