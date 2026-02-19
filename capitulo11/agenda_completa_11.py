from capitulo10.lista_unica import ListaUnica
from capitulo10.nome import Nome
from capitulo10.agenda import Telefone, TipoTelefone
import sys
import sqlite3
import os.path
from functools import total_ordering
from collections import UserList


BANCO = """
create table tipos(id integer primary key autoincrement,
                   descrição text);
create table nomes(id integer primary key autoincrement,
                   nome text);
create table telefones(id integer primary key autoincrement,
                   id_nome integer,
                   número text,
                   id_tipo integer);
insert into tipos(descrição) values ("Celular");
insert into tipos(descrição) values ("Fixo");
insert into tipos(descrição) values ("Fax");
insert into tipos(descrição) values ("Casa");
insert into tipos(descrição) values ("Trabalho");
"""


def nulo_ou_vazio(texto):
    return texto is None or not texto.strip()


def valida_faixa_inteiro(pergunta, inicio, fim, padrão=None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrão is not None:
                entrada = padrão
            valor = int(entrada)
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


def valida_faixa_inteiro_ou_branco(pergunta, inicio, fim):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada):
                return None
            valor = int(entrada)
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


class ListaÚnica(UserList):
    def __init__(self, elem_classe, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_classe

    def append(self, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().append(elem)

    def __setitem__(self, posição, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().__setitem__(posição, elem)

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("Tipo inválido")

    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.index(elem)
        except ValueError:
            return -1


class DBListaÚnica(ListaÚnica):
    def __init__(self, elem_class):
        super().__init__(elem_class)
        self.apagados = []

    def remove(self, elem):
        if elem.id is not None:
            self.apagados.append(elem.id)
        super().remove(elem)

    def limpa(self):
        self.apagados = []


@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(
            id(self), self.__nome, self.__chave, type(self).__name__
        )

    def __eq__(self, outro):
        return self.nome == outro.nome

    def __lt__(self, outro):
        return self.nome < outro.nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @property
    def chave(self):
        return self.__chave

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()


class DBNome(Nome):
    def __init__(self, nome, id_=None):
        super().__init__(nome)
        self.id = id_


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


class DBTipoTelefone(TipoTelefone):
    def __init__(self, id_, tipo):
        super().__init__(tipo)
        self.id = id_


class Telefone:
    def __init__(self, número, tipo=None):
        self.número = número
        self.tipo = tipo

    def __str__(self):
        tipo = self.tipo or ""
        return f"{self.número} {tipo}"

    def __eq__(self, outro):
        return self.número == outro.número and (
            (self.tipo == outro.tipo) or (self.tipo is None or outro.tipo is None)
        )

    @property
    def número(self):
        return self.__número

    @número.setter
    def número(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError("Número não pode ser None ou em branco")
        self.__número = valor


class DBTelefone(Telefone):
    def __init__(self, número, tipo=None, id_=None, id_nome=None):
        super().__init__(número, tipo)
        self.id = id_
        self.id_nome = id_nome


class DBTelefones(DBListaÚnica):
    def __init__(self):
        super().__init__(DBTelefone)


class DBTiposTelefone(ListaÚnica):
    def __init__(self):
        super().__init__(DBTipoTelefone)


class DBDadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = DBTelefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, DBNome):
            raise TypeError("nome deve ser uma instância da classe DBNome")
        self.__nome = valor

    def pesquisa_telefone(self, telefone):
        posição = self.telefones.pesquisa(DBTelefone(telefone))
        if posição == -1:
            return None
        else:
            return self.telefones[posição]


class DBAgenda:
    def __init__(self, banco):
        self.tiposTelefone = DBTiposTelefone()
        self.banco = banco
        novo = not os.path.isfile(banco)
        self.conexão = sqlite3.connect(banco)
        self.conexão.row_factory = sqlite3.Row
        if novo:
            self.cria_banco()
        self.carregaTipos()

    def carregaTipos(self):
        for tipo in self.conexão.execute("select * from tipos"):
            id_ = tipo["id"]
            descrição = tipo["descrição"]
            self.tiposTelefone.append(DBTipoTelefone(id_, descrição))

    def cria_banco(self):
        self.conexão.executescript(BANCO)

    def pesquisaNome(self, nome):
        if not isinstance(nome, DBNome):
            raise TypeError("nome deve ser do tipo DBNome")
        achado = self.conexão.execute(
            """select count(*)
                                         from nomes where nome = ?""",
            (nome.nome,),
        ).fetchone()
        if achado[0] > 0:
            return self.carrega_por_nome(nome)
        else:
            return None

    def carrega_por_id(self, id):
        consulta = self.conexão.execute("select * from nomes where id = ?", (id,))

        return self.carrega(consulta.fetchone())

    def carrega_por_nome(self, nome):
        consulta = self.conexão.execute(
            "select * from nomes where nome = ?", (nome.nome,)
        )
        return self.carrega(consulta.fetchone())

    def carrega(self, consulta):
        if consulta is None:
            return None
        novo = DBDadoAgenda(DBNome(consulta["nome"], consulta["id"]))
        for telefone in self.conexão.execute(
            "select * from telefones where id_nome = ?", (novo.nome.id,)
        ):
            numero_telefone = DBTelefone(
                telefone["número"], None, telefone["id"], telefone["id_nome"]
            )
            for tipo in self.tiposTelefone:
                if tipo.id == telefone["id_tipo"]:
                    numero_telefone.tipo = tipo
                    break
            novo.telefones.append(numero_telefone)
        return novo

    def lista(self):
        consulta = self.conexão.execute("select * from nomes order by nome")
        for registro in consulta:
            yield self.carrega(registro)

    def novo(self, registro):
        try:
            cur = self.conexão.cursor()
            cur.execute("insert into nomes(nome) values (?)", (str(registro.nome),))
            registro.nome.id = cur.lastrowid
            for telefone in registro.telefones:
                cur.execute(
                    """insert into telefones(número,
                               id_tipo, id_nome) values (?,?,?)""",
                    (telefone.número, telefone.tipo.id, registro.nome.id),
                )
                telefone.id = cur.lastrowid
            self.conexão.commit()
        except:
            self.conexão.rollback()
            raise
        finally:
            cur.close()

    def atualiza(self, registro):
        try:
            cur = self.conexão.cursor()
            cur.execute(
                "update nomes set nome=? where id = ?",
                (str(registro.nome), registro.nome.id),
            )
            for telefone in registro.telefones:
                if telefone.id is None:
                    cur.execute(
                        """insert into telefones(número,
                                   id_tipo, id_nome)
                                   values (?,?,?)""",
                        (telefone.número, telefone.tipo.id, registro.nome.id),
                    )
                    telefone.id = cur.lastrowid
                else:
                    cur.execute(
                        """update telefones set número=?,
                                          id_tipo=?, id_nome=?
                                          where id = ?""",
                        (
                            telefone.número,
                            telefone.tipo.id,
                            registro.nome.id,
                            telefone.id,
                        ),
                    )
            for apagado in registro.telefones.apagados:
                cur.execute("delete from telefones where id = ?", (apagado,))
            self.conexão.commit()
            registro.telefones.limpa()
        except:
            self.conexão.rollback()
            raise
        finally:
            cur.close()

    def apaga(self, registro):
        try:
            cur = self.conexão.cursor()
            cur.execute("delete from telefones where id_nome = ?", (registro.nome.id,))
            cur.execute("delete from nomes where id = ?", (registro.nome.id,))
            self.conexão.commit()
        except:
            self.conexão.rollback()
            raise
        finally:
            cur.close()


class Menu:
    def __init__(self):
        self.opções = [["Sair", None]]

    def adiciona_opção(self, nome, função):
        self.opções.append([nome, função])

    def exibe(self):
        print("====")
        print("Menu")
        print("====\n")
        for i, opção in enumerate(self.opções):
            print(f"[{i}] - {opção[0]}")
        print()

    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro(
                "Escolha uma opção: ", 0, len(self.opções) - 1
            )
            if escolha == 0:
                break
            self.opções[escolha][1]()


class AppAgenda:

    @staticmethod
    def pede_nome():
        return input("Nome: ")

    @staticmethod
    def pede_telefone():
        return input("Telefone: ")

    @staticmethod
    def mostra_dados(dados):
        print(f"Nome: {dados.nome}")
        for telefone in dados.telefones:
            print(f"Telefone: {telefone}")
        print()

    @staticmethod
    def mostra_dados_telefone(dados):
        print(f"Nome: {dados.nome}")
        for i, telefone in enumerate(dados.telefones):
            print(f"{i} - Telefone: {telefone}")
        print()

    def __init__(self, banco):
        self.agenda = DBAgenda(banco)
        self.menu = Menu()
        self.menu.adiciona_opção("Novo", self.novo)
        self.menu.adiciona_opção("Altera", self.altera)
        self.menu.adiciona_opção("Apaga", self.apaga)
        self.menu.adiciona_opção("Lista", self.lista)
        self.ultimo_nome = None

    def pede_tipo_telefone(self, padrão=None):
        for i, tipo in enumerate(self.agenda.tiposTelefone):
            print(f" {i} - {tipo} ", end=None)
        t = valida_faixa_inteiro(
            "Tipo: ", 0, len(self.agenda.tiposTelefone) - 1, padrão
        )
        return self.agenda.tiposTelefone[t]

    def pesquisa(self, nome):
        if isinstance(nome, str):
            nome = DBNome(nome)
        dado = self.agenda.pesquisaNome(nome)
        return dado

    def novo(self):
        novo = AppAgenda.pede_nome()
        if nulo_ou_vazio(novo):
            return
        nome = DBNome(novo)
        if self.pesquisa(nome) is not None:
            print("Nome já existe!")
            return
        registro = DBDadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.novo(registro)

    def apaga(self):
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        p = self.pesquisa(nome)
        if p is not None:
            self.agenda.apaga(p)
        else:
            print("Nome não encontrado.")

    def altera(self):
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        p = self.pesquisa(nome)
        if p is not None:
            print("\nEncontrado:\n")
            AppAgenda.mostra_dados(p)
            print("Digite enter caso não queira alterar o nome")
            novo = AppAgenda.pede_nome()
            if not nulo_ou_vazio(novo):
                p.nome.nome = novo
            self.menu_telefones(p)
            self.agenda.atualiza(p)
        else:
            print("Nome não encontrado!")

    def menu_telefones(self, dados):
        while True:
            print("\nEditando telefones\n")
            AppAgenda.mostra_dados_telefone(dados)
            if len(dados.telefones) > 0:
                print("\n[A] - alterar\n[D] - apagar\n", end="")
            print("[N] - novo\n[S] - sair\n")
            operação = input("Escolha uma operação: ")
            operação = operação.lower()
            if operação not in ["a", "d", "n", "s"]:
                print("Operação inválida. Digite A, D, N ou S")
                continue
            if operação == "a" and len(dados.telefones) > 0:
                self.altera_telefones(dados)
            elif operação == "d" and len(dados.telefones) > 0:
                self.apaga_telefone(dados)
            elif operação == "n":
                self.novo_telefone(dados)
            elif operação == "s":
                break

    def novo_telefone(self, dados):
        telefone = AppAgenda.pede_telefone()
        if nulo_ou_vazio(telefone):
            return
        if dados.pesquisa_telefone(telefone) is not None:
            print("Telefone já existe")
        tipo = self.pede_tipo_telefone()
        dados.telefones.append(DBTelefone(telefone, tipo))

    def apaga_telefone(self, dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a poisção do número a apagar, enter para sair: ",
            0,
            len(dados.telefones) - 1,
        )
        if t is None:
            return
        dados.telefones.remove(dados.telefones[t])

    def altera_telefones(self, dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a posição do número a alterar, enter para sair: ",
            0,
            len(dados.telefones) - 1,
        )
        if t is None:
            return
        telefone = dados.telefones[t]
        print(f"Telefone: {telefone}")
        print("Digite enter caso não queira alterar o número")
        novo_telefone = AppAgenda.pede_telefone()
        if not nulo_ou_vazio(novo_telefone):
            telefone.número = novo_telefone
        print("Digite enter caso não queira alterar o tipo")
        telefone.tipo = self.pede_tipo_telefone(
            self.agenda.tiposTelefone.pesquisa(telefone.tipo)
        )

    def lista(self):
        print("\nAgenda")
        print("-" * 60)
        for e in self.agenda.lista():
            AppAgenda.mostra_dados(e)
        print("-" * 60)

    def execute(self):
        self.menu.execute()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app = AppAgenda(sys.argv[1])
        app.execute()
    else:
        print("Erro: nome do banco de dados não informado")
        print("      agenda.py nome_do_banco")