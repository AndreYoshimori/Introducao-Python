# Exercício 10.3: Modifique a classe Televisão de forma que, se pedirmos para mudar o canal para baixo, além do mínimo, ela vá para o canal máximo.
# Se mudar o canal para cima, além do canal máximo, que volte ao canal mínimo.
# Exemplo
"""
>>> tv = Televisão(2, 10)
>>> tv.muda_canal_para_baixo()
>>> tv.canal
10
>>> tv.muda_canal_para_baixo()
>>> tv.canal
2
"""

class Televisao:
    def __init__(self, canal_min, canal_max, canal_inicial=2):
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
        

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
        else:
            self.canal = self.canal_min

tv = Televisao(1, 99, 10)
        
for x in range(0, 120):
    tv.muda_canal_para_baixo()
    print(tv.canal)

for x in range(0, 120):
    tv.muda_canal_para_cima()
    print(tv.canal)
