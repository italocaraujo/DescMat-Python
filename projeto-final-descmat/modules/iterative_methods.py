import numpy as np
import matplotlib.pyplot as plt

def metodo_jacobi(A, b, max_iter=100, tol=1e-6):
    """Resolve um sistema linear usando o Método de Jacobi."""
    n = len(b)
    x = np.zeros(n)  # Solução inicial
    erros = []       # Lista para armazenar os erros

    for it in range(max_iter):
        x_novo = np.zeros_like(x)

        for i in range(n):
            soma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_novo[i] = (b[i] - soma) / A[i, i]

        # Calcula o erro absoluto da iteração atual
        erro = np.linalg.norm(x_novo - x, ord=np.inf)
        erros.append(erro)

        # Verifica a tolerância
        if erro < tol:
            break

        x = x_novo

    return x, erros

def plotar_convergencia(erros, nome_arquivo=None):
    """Plota a convergência de um método iterativo."""
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(erros) + 1), erros, marker='o')
    plt.title("Convergência do Método de Jacobi")
    plt.xlabel("Iterações")
    plt.ylabel("Erro Absoluto")
    plt.grid()

    if nome_arquivo:
        plt.savefig(nome_arquivo)
        print(f"Gráfico salvo como '{nome_arquivo}'")
    else:
        plt.show()
