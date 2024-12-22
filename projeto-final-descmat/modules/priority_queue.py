from queue import PriorityQueue
import numpy as np

class FilaDePrioridade:
    """Fila de prioridade baseada no número de condição da matriz."""

    def __init__(self):
        self.fila = PriorityQueue()

    def adicionar(self, A, b):
        """Adiciona um sistema à fila, ordenado pelo número de condição."""
        cond = np.linalg.cond(A)
        self.fila.put((cond, (A, b)))

    def obter(self):
        """Obtém o sistema com maior prioridade (menor número de condição)."""
        return self.fila.get()[1]

    def vazia(self):
        """Verifica se a fila está vazia."""
        return self.fila.empty()

# Exemplo de uso
if __name__ == "__main__":
    fila = FilaDePrioridade()
    A1 = np.array([[4, -1], [-1, 4]])
    b1 = np.array([1, 1])

    A2 = np.array([[1, 2], [2, 3]])
    b2 = np.array([4, 7])

    fila.adicionar(A1, b1)
    fila.adicionar(A2, b2)

    while not fila.vazia():
        A, b = fila.obter()
        print("Sistema com prioridade processado:", A, b)
