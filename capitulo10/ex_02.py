# Exercício 10.2: Atualmente, a classe Televisão inicializa o canal com 2.
# Modifique a classe Televisão de forma a receber o canal inicial em seu contrutor como parâmetro opcional.

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
        
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1

tv = Televisao(1, 99, 10)
        
for x in range(0, 120):
    tv.muda_canal_para_baixo()
    print(tv.canal)

for x in range(0, 120):
    tv.muda_canal_para_cima()
    print(tv.canal)
