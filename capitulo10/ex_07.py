# Exercício 10.7: Altere a classe Televião. Ela só deve aceitar os comandos de trocar de canal se estiver ligada.

class Televisao:
    def __init__(self, canal_min=2, canal_max=14, canal_inicial=2):
        self.ligada = False
        self.canal_min = canal_min
        self.canal_max = canal_max

        if canal_min <= canal_inicial <= canal_max:
            self.canal = canal_inicial
        else:
            self.canal = canal_min

    def muda_canal_para_baixo(self):
        if self.ligada:
            if self.canal -1 >= self.canal_min:
                self.canal -= 1
            else:
                self.canal = self.canal_max
        return self.canal

    def muda_canal_para_cima(self):
        if self.ligada:
            if self.canal + 1 <= self.canal_max:
                self.canal += 1
            else:
                self.canal = self.canal_min
        return self.canal
    

class ControleRemoto:
    def __init__(self, televisao, pilha):
        self.televisao = televisao
        self.pilha = pilha
    
    def liga(self):
        if self.pilha.consuma(1):
            self.televisao.ligada = True

    def desliga(self):
        if self.pilha.consuma(1):
            self.televisao.ligada = False

    def canal_mais(self):
        if self.pilha.consuma(1):
            self.televisao.muda_canal_para_cima()

    def canal_menos(self):
        if self.pilha.consuma(1):
            self.televisao.muda_canal_para_baixo()


class Pilha:
    def __init__(self, energia=100):
        self.energia = energia
    
    def consuma(self, consumo):
        if consumo > self.energia:
            consumo = self.energia
        self.energia -= consumo
        return consumo

tv = Televisao(2, 14)
pilha = Pilha(5)
controle = ControleRemoto(tv, pilha)

print(tv.canal)
print(pilha.energia)

controle.canal_mais()
controle.canal_mais()
controle.canal_mais()
controle.canal_mais()

print(tv.canal)
print(pilha.energia)

controle.canal_mais()

print(tv.canal)
print(pilha.energia)

controle.canal_mais()

print(tv.canal)