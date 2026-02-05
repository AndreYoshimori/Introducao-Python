# Exercício 10.14: Observe o método saque das classes Conta e ContaEspecial.
# Modifique o método saque da classe Conta de forma que a verificação da possibilidade de saque seja feita por um novo método, substituindo a condição atual.
# Esse novo método retornará verdadeiro se o saque puder ser efetuado, e falso, caso contrário.
# Modifique a classe ContaEspecial de forma a trabalhar com esse novo método.
# Verifique se você ainda precisa trocar o método saque de ContaEspecial ou apenas o novo método criado para verificar a possibilidade de saque.

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

    def pode_sacar(self, valor):
        if self.saldo >= valor:
            return True
        else:
            return False

    def saque(self, valor):
        if self.pode_sacar(valor):
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
    
    def pode_sacar(self, valor):
        if self.saldo + self.limite >= valor:
            return True
        else:
            return False

    def extrato(self):
        super().extrato()
        print(f"Limite: {self.limite}")
        print(f"Total disponível para saque: {self.limite + self.saldo}")

joao = Cliente("João", "1111-1111")
maria = Cliente("Maria", "2222-2222")

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
