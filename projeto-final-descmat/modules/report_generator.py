import matplotlib.pyplot as plt
from fpdf import FPDF

def visualizar_solucoes(solucoes, nome_arquivo=None):
    """Gera gráficos para representar as soluções."""
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(solucoes) + 1), solucoes)
    plt.title("Soluções do Sistema Linear")
    plt.xlabel("Variáveis")
    plt.ylabel("Valores")
    if nome_arquivo:
        plt.savefig(nome_arquivo)
        print(f"Gráfico salvo como '{nome_arquivo}'.")
    else:
        plt.show()

def gerar_relatorio_pdf(solucoes, caminho_pdf, graficos, convergencias=None):
    """Gera um relatório em PDF com as soluções e gráficos."""
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

        if convergencias and idx < len(convergencias):
            pdf.add_page()
            pdf.cell(200, 10, txt=f"Convergência do Sistema {idx + 1}", ln=True, align='C')
            pdf.image(convergencias[idx], x=10, y=None, w=100)
            pdf.ln(10)

    pdf.output(caminho_pdf)
    print(f"Relatório PDF gerado em '{caminho_pdf}'.")
