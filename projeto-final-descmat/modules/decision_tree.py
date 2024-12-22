from sklearn.tree import DecisionTreeClassifier
import numpy as np

class ArvoreDeDecisao:
    """Árvore de decisão para determinar o método de solução."""

    def __init__(self):
        # Criar o classificador
        self.clf = DecisionTreeClassifier()

    def treinar(self, dados, rotulos):
        """Treina a árvore com dados e rótulos."""
        self.clf.fit(dados, rotulos)

    def prever(self, caracteristicas):
        """Prevê o melhor método para resolver o sistema."""
        return self.clf.predict([caracteristicas])[0]

# Exemplo de treinamento
if __name__ == "__main__":
    arvore = ArvoreDeDecisao()

    # Dados de treinamento: [dimensão, número de condição, presença de zeros]
    dados = [
        [2, 10, 1],  # Matriz pequena e bem condicionada
        [3, 500, 0], # Matriz maior e mal condicionada
        [4, 20, 1],  # Matriz moderada e bem condicionada
    ]

    # Rótulos (métodos recomendados): "cramer", "svd", "jacobi"
    rotulos = ["cramer", "svd", "jacobi"]

    # Treinar a árvore
    arvore.treinar(dados, rotulos)

    # Testar previsão
    caracteristicas = [3, 30, 0]  # Exemplo de matriz moderada e bem condicionada
    metodo = arvore.prever(caracteristicas)
    print("Melhor método recomendado:", metodo)
