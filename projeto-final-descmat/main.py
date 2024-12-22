from modules.csv_handler import carregar_sistemas_de_csv
from modules.svd_solver import processar_sistemas
from queue import Queue
import os

def principal():
    # Definição de arquivos de entrada e saída
    arquivo_entrada_csv = "sistemas.csv"
    arquivo_saida_json = "solucoes.json"

    # Garante que o diretório de relatórios existe
    os.makedirs("relatorios", exist_ok=True)
    arquivo_relatorio_pdf = "relatorios/relatorio_solucoes.pdf"

    try:
        # Carregando sistemas lineares a partir do arquivo CSV
        sistemas_csv = carregar_sistemas_de_csv(arquivo_entrada_csv)
        if not sistemas_csv:
            print("Nenhum sistema foi carregado do arquivo. Verifique o arquivo de entrada.")
            return

        # Criação de uma fila para processar os sistemas
        fila = Queue()
        for A, b in sistemas_csv:
            fila.put((A, b))

        # Processando os sistemas e gerando o relatório
        processar_sistemas(fila, arquivo_saida_json, arquivo_relatorio_pdf, salvar_graficos=True)
        print(f"Processamento concluído. Resultados salvos em:\n - {arquivo_saida_json}\n - {arquivo_relatorio_pdf}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada_csv}' não foi encontrado. Verifique o caminho e tente novamente.")
    except PermissionError:
        print(f"Erro: Permissão negada ao acessar '{arquivo_entrada_csv}'. Verifique suas permissões.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    principal()
