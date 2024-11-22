import re
import numpy as np
import matplotlib.pyplot as plt
import csv

class Polinomio:
    def __init__(self, expressao):
        """Constrói um polinômio a partir de uma string."""
        self.termos = self._parse_expressao(expressao)
    
    def _parse_expressao(self, expressao):
        """Converte a expressão algébrica para um dicionário de coeficientes e expoentes."""
        termos = {}
        expressao = expressao.replace(' ', '')  # Remove espaços
        # Expressão regular para encontrar os termos do polinômio
        padrao = r'([+-]?\d*)(x\^?(\d*))'
        
        # Adicionando o termo constante (caso exista)
        expressao = re.sub(r'([+-]?\d+)x$', r'\1x^1', expressao)
        expressao = re.sub(r'x$', r'x^1', expressao)
        expressao = re.sub(r'(?<=\d)x$', r'x^1', expressao)
        
        # Encontrar os termos
        for termo in expressao.split('+'):
            termo = termo.strip()
            if 'x' in termo:
                coef, expo = termo.split('x')
                coef = int(coef) if coef not in ('', '+', '-') else (1 if coef == '' else -1)
                expo = int(expo[2:]) if expo.startswith('^') else 1
                termos[expo] = coef
            else:
                termos[0] = int(termo)
        return termos


    def __add__(self, outro):
        """Soma dois polinômios."""
        resultado = self.termos.copy()
        for expoente, coeficiente in outro.termos.items():
            if expoente in resultado:
                resultado[expoente] += coeficiente
            else:
                resultado[expoente] = coeficiente
        return Polinomio(self._formatar_polinomio(resultado))

    def __sub__(self, outro):
        """Subtrai dois polinômios."""
        resultado = self.termos.copy()
        for expoente, coeficiente in outro.termos.items():
            if expoente in resultado:
                resultado[expoente] -= coeficiente
            else:
                resultado[expoente] = -coeficiente
        return Polinomio(self._formatar_polinomio(resultado))

    def __mul__(self, outro):
        """Multiplica dois polinômios."""
        resultado = {}
        for expoente1, coeficiente1 in self.termos.items():
            for expoente2, coeficiente2 in outro.termos.items():
                expoente_resultante = expoente1 + expoente2
                coeficiente_resultante = coeficiente1 * coeficiente2
                if expoente_resultante in resultado:
                    resultado[expoente_resultante] += coeficiente_resultante
                else:
                    resultado[expoente_resultante] = coeficiente_resultante
        return Polinomio(self._formatar_polinomio(resultado))

    def __eq__(self, outro):
        """Verifica se dois polinômios são iguais."""
        return self.termos == outro.termos

    def avaliar(self, x):
        """Avalia o polinômio para um valor de x."""
        resultado = 0
        for expoente, coeficiente in self.termos.items():
            resultado += coeficiente * (x ** expoente)
        return resultado

    def _formatar_polinomio(self, termos):
        """Formata os termos do polinômio para uma string legível."""
        termos_formatados = []
        for expoente in sorted(termos.keys(), reverse=True):
            coeficiente = termos[expoente]
            if coeficiente == 0:
                continue
            elif expoente == 0:
                termos_formatados.append(f'{coeficiente}')
            elif expoente == 1:
                termos_formatados.append(f'{coeficiente}x')
            else:
                termos_formatados.append(f'{coeficiente}x^{expoente}')
        return ' + '.join(termos_formatados).replace(' + -', ' - ')

    def __str__(self):
        """Representação legível do polinômio."""
        return self._formatar_polinomio(self.termos)

    def plotar(self, intervalo=(-10, 10), passos=100):
        """Plota o gráfico do polinômio no intervalo dado."""
        x = np.linspace(intervalo[0], intervalo[1], passos)
        y = [self.avaliar(xi) for xi in x]
        
        plt.plot(x, y, label=str(self))
        plt.title(f'Gráfico do Polinômio: {str(self)}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.show()

    def salvar_csv(self, intervalo=(-10, 10), passos=100, nome_arquivo="polinomio.csv"):
        """Salva os dados do gráfico em um arquivo CSV."""
        x = np.linspace(intervalo[0], intervalo[1], passos)
        y = [self.avaliar(xi) for xi in x]
        
        with open(nome_arquivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["x", "f(x)"])
            for xi, yi in zip(x, y):
                writer.writerow([xi, yi])

# Exemplo de uso
polinomio1 = Polinomio("2x^2 + 3x - 5")
polinomio2 = Polinomio("x^2 - 2x + 1")

print("Polinômio 1:", polinomio1)
print("Polinômio 2:", polinomio2)

# Operações
soma = polinomio1 + polinomio2
subtracao = polinomio1 - polinomio2
multiplicacao = polinomio1 * polinomio2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)

# Avaliação para x = 3
print("Avaliação do Polinômio 1 para x = 3:", polinomio1.avaliar(3))

# Comparação entre polinômios
print("Polinômios iguais?", polinomio1 == polinomio2)

# Plotagem
polinomio1.plotar(intervalo=(-10, 10), passos=200)

# Salvar os dados em um arquivo CSV
polinomio1.salvar_csv(intervalo=(-10, 10), passos=200, nome_arquivo="polinomio1.csv")
