import numpy as np
import matplotlib.pyplot as plt
from queue import Queue
import pandas as pd

def carregar_sistemas_de_csv(caminho_arquivo):
    """Carrega sistemas lineares de um arquivo CSV com validação de valores."""
    try:
        data = pd.read_csv(caminho_arquivo)
        num_variaveis = len(data.columns) - 1  # Todas as colunas menos a última são coeficientes

        sistemas = []
        for _, row in data.iterrows():
            try:
                A = row[:num_variaveis].values.reshape(num_variaveis, num_variaveis).astype(float)
                b = row[num_variaveis:].values.astype(float)
                sistemas.append((A, b))
            except ValueError:
                print(f"Erro ao processar linha: {row.values}. Ignorando...")
        return sistemas

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro inesperado ao carregar arquivo: {e}")
        return []

def salvar_solucoes_em_csv(caminho_arquivo, solucoes):
    """Salva as soluções em um arquivo CSV."""
    try:
        df = pd.DataFrame(solucoes, columns=["x" + str(i+1) for i in range(len(solucoes[0]))])
        df.to_csv(caminho_arquivo, index=False)
        print(f"Soluções salvas em '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar soluções: {e}")

def sistema_mal_condicionado(A, limiar=1e10):
    """Verifica se a matriz do sistema é mal condicionada."""
    cond = np.linalg.cond(A)
    return cond > limiar, cond

def resolver_cramer(A, b):
    """Resolve o sistema linear usando a Regra de Cramer."""
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("Determinante da matriz principal é zero. Sistema sem solução única.")
    
    solucoes = []
    for i in range(A.shape[1]):
        Ai = np.copy(A)
        Ai[:, i] = b
        solucoes.append(np.linalg.det(Ai) / det_A)
    return np.array(solucoes)

def visualizar_solucoes(solucoes):
    """Gera gráficos para representar as soluções."""
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(solucoes) + 1), solucoes, tick_label=[f"x{i+1}" for i in range(len(solucoes))])
    plt.title("Soluções do Sistema Linear")
    plt.xlabel("Variáveis")
    plt.ylabel("Valores")
    plt.show()

def processar_sistemas(fila, arquivo_saida):
    """Processa sistemas lineares de uma fila e salva as soluções em um arquivo."""
    todas_solucoes = []
    while not fila.empty():
        A, b = fila.get()
        try:
            mal_condicionado, cond = sistema_mal_condicionado(A)
            if mal_condicionado:
                print(f"Sistema mal condicionado detectado (Número de condição: {cond:.2e}). Solução pode ser imprecisa.")
            
            solucoes = resolver_cramer(A, b)
            print("Soluções:", solucoes)
            visualizar_solucoes(solucoes)
            todas_solucoes.append(solucoes)
        except ValueError as e:
            print(f"Erro ao resolver sistema: {e}")
    salvar_solucoes_em_csv(arquivo_saida, todas_solucoes)

def principal():
    arquivo_entrada = "sistemas.csv"  # Arquivo CSV de entrada
    arquivo_saida = "solucoes.csv"  # Arquivo CSV de saída

    sistemas = carregar_sistemas_de_csv(arquivo_entrada)
    fila = Queue()
    
    # Adiciona sistemas válidos à fila
    for A, b in sistemas:
        fila.put((A, b))
    
    processar_sistemas(fila, arquivo_saida)

if __name__ == "__main__":
    principal()
