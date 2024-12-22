import pandas as pd
import numpy as np
import json

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

def salvar_solucoes_em_json(caminho_arquivo, solucoes):
    """Salva as soluções em um arquivo JSON."""
    try:
        with open(caminho_arquivo, 'w') as f:
            json.dump(solucoes, f, indent=4)
        print(f"Soluções salvas em '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar soluções: {e}")
