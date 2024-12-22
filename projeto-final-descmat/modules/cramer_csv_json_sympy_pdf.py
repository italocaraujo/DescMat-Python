import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from queue import Queue
import pandas as pd
import json
from sympy import Matrix
from fpdf import FPDF

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
    except Exception as e:
        print(f"Erro ao carregar arquivo CSV: {e}")
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

def gerar_relatorio_pdf(solucoes, caminho_pdf, graficos):
    """Gera um relatório em PDF com as soluções e análise."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatório de Soluções de Sistemas Lineares", ln=True, align='C')
    pdf.ln(10)

    for idx, item in enumerate(solucoes):
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, f"Sistema {idx + 1}:", ln=True)
        pdf.multi_cell(0, 10, f"Soluções: {item['solucoes']}")
        pdf.multi_cell(0, 10, f"Análise: {item['metodo']}. Número de condição: {item['condicao']:.2e}")
        pdf.ln(5)

        if graficos and idx < len(graficos):
            pdf.image(graficos[idx], x=10, y=None, w=100)
            pdf.ln(60)

    pdf.output(caminho_pdf)
    print(f"Relatório PDF gerado em '{caminho_pdf}'.")

def processar_sistemas(fila, arquivo_saida_json, arquivo_relatorio_pdf, salvar_graficos=False):
    """Processa sistemas lineares de uma fila e gera relatório em PDF."""
    todas_solucoes = []
    graficos = []
    while not fila.empty():
        A, b = fila.get()
        try:
            mal_condicionado, cond = sistema_mal_condicionado(A)
            if mal_condicionado:
                print(f"Sistema mal condicionado detectado (Número de condição: {cond:.2e}). Usando SVD.")
                solucoes = resolver_svd(A, b)
                metodo = "Resolvido com SVD (decomposição para maior estabilidade)"
            else:
                solucoes = resolver_svd(A, b)
                metodo = "Resolvido com Regra de Cramer (SVD como método secundário)"

            print("Soluções:", solucoes)
            if salvar_graficos:
                nome_grafico = f"grafico_sistema_{len(todas_solucoes)+1}.png"
                visualizar_solucoes(solucoes, nome_arquivo=nome_grafico)
                graficos.append(nome_grafico)
            todas_solucoes.append({"solucoes": solucoes.tolist(), "metodo": metodo, "condicao": cond})
        except ValueError as e:
            print(f"Erro ao resolver sistema: {e}")
    
    salvar_solucoes_em_json(arquivo_saida_json, todas_solucoes)
    gerar_relatorio_pdf(todas_solucoes, arquivo_relatorio_pdf, graficos)

def principal():
    arquivo_entrada_csv = "sistemas.csv"
    arquivo_saida_json = "solucoes.json"
    arquivo_relatorio_pdf = "relatorio_solucoes.pdf"

    sistemas_csv = carregar_sistemas_de_csv(arquivo_entrada_csv)
    fila = Queue()
    
    for A, b in sistemas_csv:
        fila.put((A, b))
    
    processar_sistemas(fila, arquivo_saida_json, arquivo_relatorio_pdf, salvar_graficos=True)

if __name__ == "__main__":
    principal()