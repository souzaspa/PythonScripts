# Fila em Python: FIFO -> First in First out

class Fila:
    def __init__(self):
        self.fila = []

    # Inserir um elemento na fila
    def inserir(self, num):
        self.fila.append(num)

    # Excluir um elemento na fila
    def excluir(self):
        if not self.vazia():
            return self.fila.pop(0)

    # Deletar toda fila: Terá que ser instanciada novamente
    def delete(self):
        del self.fila

    # Mostrar os elementos da fila
    def mostrar_fila(self):
        for item in self.fila:
            print(item, end=' ')

    # Mostrar o tamanho da fila
    def tamanho(self):
        return len(self.fila)

    # Fila vazia: retorna true. Fila com elementos: retorna false
    def vazia(self):
        return self.tamanho() == 0


# Exemplo
fila = Fila()

fila.inserir(4)
fila.inserir(7)
fila.inserir(14)
fila.inserir(9)
fila.inserir(2)
fila.mostrar_fila()
print('\n')

# print(fila.tamanho())
# print('\n')

# print(fila.vazia())
# print('\n')

fila.excluir()
fila.mostrar_fila()

