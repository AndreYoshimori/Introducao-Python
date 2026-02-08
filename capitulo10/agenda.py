from functools import total_ordering
from lista_unica import ListaUnica
from nome import Nome


@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"({self.tipo})"
    
    def __eq__(self, outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo
    
    def __lt__(self, outro):
        return self.tipo < outro.tipo
    

class Telefone:
    def __init__(self, numero, tipo=None):
        self.numero = numero
        self.tipo = tipo

    def __str__(self):
        tipo = self.tipo or ""
        return f"{self.numero} {tipo}"
    
    def __eq__(self, outro):
        return self.numero == outro.numero and ((self.tipo == outro.tipo) or (self.tipo is None or outro.tipo is None))

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, valor):
        if valor is None or not valor.strip():
            raise ValueError("Número não pode ser None ou em branco")
        self.__numero = valor


class Telefones(ListaUnica):
    def __init__(self):
        super().__init__(Telefone)


class DadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = Telefones()

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, Nome):
            raise TypeError("nome deve ser uma instância da classe Nome")
        self.__nome = valor

    def pesquisa_telefone(self, telefone):
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]
        

class TiposTelefone(ListaUnica):
    def __init__(self):
        super().__init__(TipoTelefone)


class Agenda(ListaUnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tipos_telefone = TiposTelefone()

    def adiciona_tipo(self, tipo):
        self.tipos_telefone.append(TipoTelefone(tipo))

    def pesquisaNome(self, nome):
        if isinstance(nome, str):
            nome = Nome(nome)
        for dados in self.data:
            if dados.nome == nome:
                return dados
        return None

    def ordena(self):
        self.data.sort(key=lambda dado: str(dado.nome))


class Menu:
    def __init__(self):
        self.opcoes = [["Sair", None]]

    def adicionaopcao(self, nome, funcao):
        self.opcoes.append([nome, funcao])

    def exibe(self):
        print("====")
        print("Menu")
        print("====\n")
        
        for i, opcao in enumerate(self.opcoes):
            print(f"[{i}] - {opcao[0]}")
        print()

    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro("Escolha uma opção: ",
                                           0, len(self.opcoes)-1)
            if escolha == 0:
                break
            self.opcoes[escolha][1]()


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")