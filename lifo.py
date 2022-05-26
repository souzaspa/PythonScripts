# Pilha em Python: LIFO -> Last in First out

class Pilha:
    def __init__(self):
        self.pilha = []

    # Inserir um elemento na pilha
    def inserir(self, num):
        self.pilha.append(num)

    # Excluir um elemento da pilha
    def excluir(self):
        self.pilha.pop()

    # Deletar a pilha
    def deletar(self):
        del self.pilha

    # Mostrar os elementos da fila
    def mostrar_pilha(self):
        for item in self.pilha:
            print(item, end=' ')

    # Mostrar o tamanho da pilha
    def tamanho(self):
        return len(self.pilha)

    # Pilha vazia: retorna true. Pilha com elementos: retorna false
    def vazia(self):
        return self.tamanho() == 0


# Exemplo
pilha = Pilha()

pilha.inserir(3)
pilha.inserir(13)
pilha.inserir(23)
pilha.inserir(33)
pilha.inserir(43)

pilha.mostrar_pilha()
print('\n')

pilha.excluir()
pilha.mostrar_pilha()

print('\n')

pilha.excluir()
pilha.mostrar_pilha()
