# Exercício 10.4: Utilizando o que aprendemos com funções, modifique o construtor da classe Televisão de forma 
# que canal_min e canal_max sejam parâmetro opcionais, em que canal_min vale 2 e canal_max vale 14, 
# caso outro valor não seja passado.

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

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
        else:
            self.canal = self.canal_min

tv = Televisao()
        
for x in range(0, 120):
    tv.muda_canal_para_baixo()
    print(tv.canal)

for x in range(0, 120):
    tv.muda_canal_para_cima()
    print(tv.canal)
