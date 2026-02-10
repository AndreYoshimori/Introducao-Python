from clientes import Cliente
from contas import Conta, ContaEspecial


joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta1 = Conta([joão], numero="001", saldo=1000)
conta2 = ContaEspecial([maria, joão], numero="002", saldo=500, limite=1000)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
