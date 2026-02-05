# Exercício 10.12: Modifique as classes Conta e ContaEspecial para que a operação de saque 
# retorne verdadeiro se o saque foi efetuado e falso, caso contrário.

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
        
joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta_comum = Conta([joao], numero="001", saldo=100)
conta_especial = ContaEspecial([maria], numero="002", saldo=100, limite=200)

print("Conta comum")
print(conta_comum.saque(80))
print(conta_comum.saque(50))
conta_comum.extrato()

print("Conta especial")
print(conta_especial.saque(250))
print(conta_especial.saque(60))
conta_especial.extrato()