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
        if self.canal -1 >= self.canal_min:
            self.canal -= 1
        else:
            self.canal = self.canal_max
        return self.canal

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
        else:
            self.canal = self.canal_min
        return self.canal
    

class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao
    
    def liga(self):
        self.televisao.ligada = True

    def desliga(self):
        self.televisao.ligada = False

    def canal_mais(self):
        self.televisao.muda_canal_para_cima()

    def canal_menos(self):
        self.televisao.muda_canal_para_baixo()

tv = Televisao(2, 14)
controle = ControleRemoto(tv)

print(tv.canal)

controle.canal_mais()
print(tv.canal)

print(tv.ligada)

controle.liga()
print(tv.ligada)
