import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from queue import Queue
import pandas as pd
import json
from sympy import Matrix
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def carregar_sistemas_de_csv(caminho_arquivo):
    """Carrega sistemas lineares de um arquivo CSV com validação de valores."""
    try:
        data = pd.read_csv(caminho_arquivo)
        num_variaveis = len(data.columns) - 1
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

def salvar_solucoes_em_json(caminho_arquivo, solucoes):
    """Salva as soluções em um arquivo JSON."""
    try:
        with open(caminho_arquivo, 'w') as f:
            json.dump(solucoes, f, indent=4)
        print(f"Soluções salvas em '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar soluções: {e}")

def sistema_mal_condicionado(A, limiar=1e10):
    """Verifica se a matriz do sistema é mal condicionada."""
    cond = np.linalg.cond(A)
    return cond > limiar, cond

def resolver_svd(A, b):
    """Resolve o sistema linear utilizando decomposição SVD para maior estabilidade."""
    U, S, Vt = np.linalg.svd(A)
    S_inv = np.diag(1 / S)
    x = Vt.T @ S_inv @ U.T @ b
    return x

def visualizar_solucoes(solucoes, nome_arquivo=None):
    """Gera gráficos para representar as soluções."""
    plt.figure(figsize=(8, 6))
    sns.barplot(x=[f"x{i+1}" for i in range(len(solucoes))], y=solucoes)
    plt.title("Soluções do Sistema Linear")
    plt.xlabel("Variáveis")
    plt.ylabel("Valores")
    if nome_arquivo:
        plt.savefig(nome_arquivo)
        print(f"Gráfico salvo como '{nome_arquivo}'.")
    else:
        plt.show()

def criar_relatorio_pdf(nome_arquivo, sistemas, solucoes):
    """Gera um relatório em PDF com os resultados e gráficos."""
    doc = SimpleDocTemplate(nome_arquivo)
    estilo = getSampleStyleSheet()
    elementos = []

    # Título
    elementos.append(Paragraph("Relatório de Sistemas Lineares", estilo['Title']))
    elementos.append(Spacer(1, 20))

    for i, (sistema, solucao) in enumerate(zip(sistemas, solucoes)):
        A, b = sistema
        elementos.append(Paragraph(f"Sistema {i+1}", estilo['Heading2']))
        elementos.append(Paragraph(f"Matriz A: {A.tolist()}", estilo['Normal']))
        elementos.append(Paragraph(f"Vetor b: {b.tolist()}", estilo['Normal']))
        elementos.append(Paragraph(f"Soluções: {solucao['solucoes']}", estilo['Normal']))

        # Adiciona gráfico
        caminho_grafico = f"grafico_sistema_{i+1}.png"
        try:
            elementos.append(Image(caminho_grafico, width=400, height=300))
        except Exception as e:
            elementos.append(Paragraph(f"Erro ao adicionar gráfico: {e}", estilo['Normal']))
        elementos.append(Spacer(1, 20))

    # Salvar PDF
    doc.build(elementos)
    print(f"Relatório salvo como '{nome_arquivo}'.")

def processar_sistemas(fila, arquivo_saida, salvar_graficos=False):
    """Processa sistemas lineares de uma fila e salva as soluções em um arquivo."""
    todas_solucoes = []
    sistemas_resolvidos = []
    while not fila.empty():
        A, b = fila.get()
        try:
            mal_condicionado, cond = sistema_mal_condicionado(A)
            if mal_condicionado:
                print(f"Sistema mal condicionado detectado (Número de condição: {cond:.2e}). Usando SVD para maior estabilidade.")
                solucoes = resolver_svd(A, b)
            else:
                solucoes = resolver_svd(A, b)

            print("Soluções:", solucoes)
            if salvar_graficos:
                nome_grafico = f"grafico_sistema_{len(todas_solucoes)+1}.png"
                visualizar_solucoes(solucoes, nome_arquivo=nome_grafico)
            else:
                visualizar_solucoes(solucoes)

            todas_solucoes.append({"solucoes": solucoes.tolist()})
            sistemas_resolvidos.append((A, b))
        except ValueError as e:
            print(f"Erro ao resolver sistema: {e}")
    salvar_solucoes_em_json(arquivo_saida, todas_solucoes)
    return sistemas_resolvidos, todas_solucoes

def principal():
    arquivo_entrada_csv = "sistemas.csv"
    arquivo_saida_json = "solucoes.json"
    arquivo_saida_pdf = "relatorio_sistemas.pdf"

    sistemas_csv = carregar_sistemas_de_csv(arquivo_entrada_csv)
    fila = Queue()

    # Adiciona sistemas válidos à fila
    for A, b in sistemas_csv:
        fila.put((A, b))
    
    sistemas_resolvidos, solucoes = processar_sistemas(fila, arquivo_saida_json, salvar_graficos=True)
    criar_relatorio_pdf(arquivo_saida_pdf, sistemas_resolvidos, solucoes)

if __name__ == "__main__":
    principal()
