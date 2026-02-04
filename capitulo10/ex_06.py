# Exercício 10.6: Modifique a classe Televisão de forma que os métodos muda_canal_para_cima e muda_canal_para_baixo retornem o canal após a mudança.

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

tv_sala = Televisao(canal_min=1, canal_max = 99)
print("Canais da TV da sala:")
for x in range(0, 120):
    print(tv_sala.muda_canal_para_baixo())

tv_quarto = Televisao(canal_min = 5, canal_max = 50)
print("\nCanais da TV do quarto:")
for x in range(0, 120):
    print(tv_quarto.muda_canal_para_cima())
