# Exercício 10.11: Crie classes para representar estados e cidades.
# Cada estado tem um nome, sigla, e cidades.
# Cada cidade tem nome e população.
# Escreva um programa de testes que crie três estados com algumas cidades em cada um.
# Exiba a população de cada estado como a soma da população de suas cidades.

class Estado:
    def __init__(self, nome, sigla, cidades=None):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades if cidades is not None else []

    def adiciona_cidade(self, cidade):
        self.cidades.append(cidade)
    
    def mostra_populacao(self):
        populacao_total = 0
        for cidade in self.cidades:
            populacao_total += cidade.populacao
        print(f"População total de {self.nome}: {populacao_total}")


class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

atibaia = Cidade("Atibaia", 167161)
guaruja = Cidade("Guarujá", 287634)
campinas = Cidade("Campinas", 1200000)
sao_paulo = Estado("São Paulo", "SP", [atibaia, guaruja, campinas])

serra = Cidade("Serra", 521000)
vila_velha = Cidade("Vila Velha", 468000)
vitoria = Cidade("Vitória", 323000)
espirito_santo = Estado("Espírito Santo", "ES", [serra, vila_velha, vitoria])

rio_grande_do_sul = Estado("Rio Grande do Sul", "RS")
porto_alegre = Cidade("Porto Alegre", 1388794)
gramado = Cidade("Gramado", 40134)
canela = Cidade("Canela", 50715)
rio_grande_do_sul.adiciona_cidade(porto_alegre)
rio_grande_do_sul.adiciona_cidade(gramado)
rio_grande_do_sul.adiciona_cidade(canela)

sao_paulo.mostra_populacao()
espirito_santo.mostra_populacao()
rio_grande_do_sul.mostra_populacao()
