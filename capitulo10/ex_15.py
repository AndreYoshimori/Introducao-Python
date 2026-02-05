# Exercício 10.15: Modifique a classe ListaUnica para sobrescrever o método extend de UserList.
# extend funciona como o append, mas recebe uma lista como parâmetro.
# Verifique o tipo de cada elemento na lista antes de adicioná-lo à lista.

from collections import UserList


class ListaUnica(UserList):
    def __init__(self, elem_classe, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_classe
    
    def append(self, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().append(elem)

    def __setitem__(self, posicao, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().__setitem_(posicao, elem)
    
    def extend(self, lista_elem):
        for e in lista_elem:
            self.append(e)

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("Tipo inválido.")

lu = ListaUnica(int)

lu.append(5)
lu.append(3)
print(lu)

lu.extend([8, 4, 5, 2, 3])
print(lu)
