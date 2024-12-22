from modules.csv_handler import salvar_solucoes_em_json
from modules.report_generator import gerar_relatorio_pdf
from modules.svd_solver import resolver_svd, sistema_mal_condicionado
from modules.report_generator import visualizar_solucoes
from queue import Queue

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
