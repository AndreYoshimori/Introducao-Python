# Exercício 10.1: Adicione os atributos tamanho e marca à classe Televisão.
# Crie dois objetos Televisão e atribua tamanhos e marcas diferentes.
# Depois, imprima o valor desses atributos de forma a confirmar a independência dos valores de cada instância (objeto).

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 40
        self.marca = "LG"

tv_quarto = Televisao()
tv_quarto.tamanho = 32
tv_quarto.marca = "Samsung"

tv_sala = Televisao()
tv_sala.tamanho = 55
tv_sala.marca = "Philips"

print(f"Tamanho da TV do quarto: {tv_quarto.tamanho}")
print(f"Tamanho da TV da sala: {tv_sala.tamanho}")

print(f"Marca da TV do quarto: {tv_quarto.marca}")
print(f"Marca da TV do sala: {tv_sala.marca}")
