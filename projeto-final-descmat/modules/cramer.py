import numpy as np
import matplotlib.pyplot as plt
from queue import Queue

def gerar_sistema_linear(num_variaveis=3):
    """Gera coeficientes e termos independentes para um sistema linear."""
    A = np.random.randint(-10, 10, (num_variaveis, num_variaveis))
    b = np.random.randint(-10, 10, num_variaveis)
    return A, b

def resolver_cramer(A, b):
    """Resolve o sistema linear usando a Regra de Cramer."""
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("O determinante da matriz principal é zero. Sistema sem solução única.")
    
    solucoes = []
    for i in range(A.shape[1]):
        Ai = np.copy(A)
        Ai[:, i] = b
        solucoes.append(np.linalg.det(Ai) / det_A)
    return np.array(solucoes)

def visualizar_solucoes(A, b, solucoes):
    """Gera gráficos para representar as soluções."""
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(solucoes) + 1), solucoes, tick_label=[f"x{i+1}" for i in range(len(solucoes))])
    plt.title("Soluções do Sistema Linear")
    plt.xlabel("Variáveis")
    plt.ylabel("Valores")
    plt.show()

def processar_sistemas(fila):
    """Processa sistemas lineares de uma fila."""
    while not fila.empty():
        A, b = fila.get()
        try:
            solucoes = resolver_cramer(A, b)
            print("Soluções:", solucoes)
            visualizar_solucoes(A, b, solucoes)
        except ValueError as e:
            print(e)

def principal():
    num_sistemas = 3
    fila = Queue()
    
    # Gerando sistemas e adicionando na fila
    for _ in range(num_sistemas):
        A, b = gerar_sistema_linear()
        fila.put((A, b))
    
    processar_sistemas(fila)

if __name__ == "__main__":
    principal()
