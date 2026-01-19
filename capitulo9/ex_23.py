# Exercício 9.23: Altere o programa para ler a última agenda lida ou gravada ao inicializar.
# Dica: utilize outro arquivo para armazenar o nome.

agenda = []

alterada = False

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
    global alterada

    alterada = True
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])


def apaga():
    global alterada

    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirmacao("Confirma a exclusão deste contato? [S/N]"):
            del agenda[p]
            print("Contato excluído com sucesso!")
            alterada = True
        else:
            print("Exclusão cancelada.")
    else:
        print("Nome não encontrado.")

    
def altera():
    global alterada

    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        if confirmacao("Confirma a alteração dos dados deste contato? [S/N]"):
            agenda[p] = [nome, telefone]
            print("Alterações feitas com sucesso!")
            alterada = True
        else:
            print("Alteração cancelada.")
    else:
        print("Nome não encontrado.")

    
def lista():
    print("\nAgenda\n\n------")
    for p, e in enumerate(agenda):
        print(f"{p}. ", end="")
        mostra_dados(e[0], e[1])
    print("------\n")


def le():
    global agenda
    global alterada

    if len(agenda) > 0 and alterada:
        if not confirmacao("Você ainda tem contatos ou alterações não salvas na sua agenda atual. Deseja mesmo assim continuar com a leitura? [S/N]"):
            print("Leitura cancelada.")
            return

    nome_arquivo = pede_nome_arquivo()

    with open("dados/ultimo_arquivo.txt", "w", encoding="utf-8") as arquivo_controle:
        arquivo_controle.write(nome_arquivo)

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split("#")
            agenda.append([nome, telefone])
        alterada = False
        

def le_inicial():
    with open("dados/ultimo_arquivo.txt", "a+", encoding="utf-8") as arquivo_controle:
        arquivo_controle.seek(0)
        linhas_arquivo = arquivo_controle.readlines()
        if linhas_arquivo:
            nome_arquivo = linhas_arquivo[0].strip()
        else:
            return

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split("#")
            agenda.append([nome, telefone])


def grava():
    global alterada

    nome_arquivo = pede_nome_arquivo()

    with open("dados/ultimo_arquivo.txt", "w", encoding="utf-8") as arquivo_controle:
        arquivo_controle.write(nome_arquivo)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")
    alterada = False


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")
            

def ordena():
    agenda.sort(key=lambda item: item[0].lower())


def confirmacao(msg):
    entrada = input(msg).lower()
    if entrada == "s":
        return True
    

def menu():
    print(f"""
  A agenda está com {len(agenda)} contato(s).

  1 - Novo
  2 - Altera
  3 - Apaga
  4-  Lista
  5 - Grava
  6 - Lê
  7 - Ordena agenda em ordem alfabética
          
  0 - Sai
""")
    
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

le_inicial()

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
    elif opcao == 7:
        ordena()
        