import math

def menu():
    opcoes = [
        "1. Soma",
        "2. Subtração",
        "3. Multiplicação",
        "4. Divisão",
        "5. Potenciação",
        "6. Radiciação",
        "9. Exponencial (e^x)",
        "19. Módulo",
        "20. Divisão Inteira",
        "21. Conversão de Graus para Radianos",
        "22. Conversão de Radianos para Graus",
        "23. Cálculo de Hipotenusa",
        "24. Arredondamento (round)",
        "25. Arredondamento para Cima (ceil)",
        "26. Arredondamento para Baixo (floor)",
        "27. Maior/Menor de Dois",
        "28. Cálculo da Distância Entre Dois Pontos",
        "29. Cálculo de Determinante de Matriz 2x2",
        "30. Solução de Equação de Primeiro Grau",
        "31. Cálculo de Área e Perímetro de Retângulo",
        "32. Cálculo de Área e Perímetro de Círculo",
        "33. Verificação de Triângulo (Desigualdade Triangular)",
        "34. Verificação de Números Primos",
        "35. Conversor de Unidades",
        "36. Calculadora de Juros Simples",
        "37. Calculadora de Juros Compostos",
        "38. Soma de Números Naturais (usando Recursão)",
        "39. Fatorial de um Número (usando Recursão)",
        "40. Permutação",
        "41. Combinação",
        "42. Conversor de Bases Numéricas",
        "43. Cálculo de Média",
        "44. Cálculo de Desvio Padrão",
        "45. Calcular Tangente de uma Reta Dados os Coeficientes",
        "0. Sair"
    ]
    
    print("Escolha a operação desejada:")
    for opcao in opcoes:
        print(opcao)

def executar_operacao(escolha):
    if escolha == 1:
        a, b = ler_dois_numeros()
        print(f"Soma: {soma(a, b)}")
    elif escolha == 2:
        a, b = ler_dois_numeros()
        print(f"Subtração: {subtracao(a, b)}")
    elif escolha == 3:
        a, b = ler_dois_numeros()
        print(f"Multiplicação: {multiplicacao(a, b)}")
    elif escolha == 4:
        a, b = ler_dois_numeros()
        print(f"Divisão: {divisao(a, b)}")
    elif escolha == 5:
        base, expoente = ler_dois_numeros("Digite a base: ", "Digite o expoente: ")
        print(f"Potenciação: {potenciacao(base, expoente)}")
    elif escolha == 6:
        num = float(input("Digite o número: "))
        grau = float(input("Digite o grau da raiz: "))
        print(f"Radiciação: {radiciacao(num, grau)}")
    elif escolha == 9:
        x = float(input("Digite o valor de x: "))
        print(f"Exponencial (e^x): {exponencial(x)}")
    elif escolha == 19:
        a, b = ler_dois_numeros()
        print(f"Módulo: {modulo(a, b)}")
    elif escolha == 20:
        a, b = ler_dois_inteiros()
        print(f"Divisão Inteira: {divisao_inteira(a, b)}")
    elif escolha == 21:
        graus = float(input("Digite o valor em graus: "))
        print(f"Radianos: {graus_para_radianos(graus)}")
    elif escolha == 22:
        radianos = float(input("Digite o valor em radianos: "))
        print(f"Graus: {radianos_para_graus(radianos)}")
    elif escolha == 23:
        cateto1, cateto2 = ler_dois_numeros("Digite o valor do primeiro cateto: ", "Digite o valor do segundo cateto: ")
        print(f"Hipotenusa: {hipotenusa(cateto1, cateto2)}")
    elif escolha == 24:
        valor = float(input("Digite o valor a ser arredondado: "))
        print(f"Arredondamento: {arredondamento(valor)}")
    elif escolha == 25:
        valor = float(input("Digite o valor a ser arredondado para cima: "))
        print(f"Arredondamento para Cima: {arredondamento_para_cima(valor)}")
    elif escolha == 26:
        valor = float(input("Digite o valor a ser arredondado para baixo: "))
        print(f"Arredondamento para Baixo: {arredondamento_para_baixo(valor)}")
    elif escolha == 27:
        a, b = ler_dois_numeros()
        resultado = maior_menor(a, b)
        print(f"Maior: {resultado['maior']}, Menor: {resultado['menor']}")
    elif escolha == 28:
        x1, y1, x2, y2 = ler_quatro_numeros("Digite a coordenada x1: ", "Digite a coordenada y1: ", 
                                             "Digite a coordenada x2: ", "Digite a coordenada y2: ")
        print(f"Distância Entre Pontos: {distancia_pontos(x1, y1, x2, y2)}")
    elif escolha == 29:
        a, b, c, d = ler_quatro_numeros("Digite o elemento a da matriz 2x2: ", "Digite o elemento b da matriz 2x2: ",
                                         "Digite o elemento c da matriz 2x2: ", "Digite o elemento d da matriz 2x2: ")
        print(f"Determinante da Matriz 2x2: {determinante_matriz_2x2(a, b, c, d)}")
    elif escolha == 30:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        print(f"Solução da Equação de Primeiro Grau: {equacao_primeiro_grau(a, b)}")
    elif escolha == 31:
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area, perimetro = area_perimetro_retangulo(largura, altura)
        print(f"Área: {area}, Perímetro: {perimetro}")
    elif escolha == 32:
        raio = float(input("Digite o raio do círculo: "))
        area, perimetro = area_perimetro_circulo(raio)
        print(f"Área: {area}, Perímetro: {perimetro}")
    elif escolha == 33:
        a, b, c = ler_tres_numeros("Digite o lado a do triângulo: ", "Digite o lado b do triângulo: ", "Digite o lado c do triângulo: ")
        if verificar_triangulo(a, b, c):
            print("Os valores formam um triângulo.")
        else:
            print("Os valores não formam um triângulo.")
    elif escolha == 34:
        num = int(input("Digite um número para verificar se é primo: "))
        if verificar_numero_primo(num):
            print(f"{num} é um número primo.")
        else:
            print(f"{num} não é um número primo.")
    elif escolha == 35:
        valor = float(input("Digite o valor a ser convertido: "))
        unidade = input("Digite a unidade de conversão (milhas_para_quilometros ou metros_para_pes): ")
        print(f"Resultado da conversão: {conversor_unidades(valor, unidade)}")
    elif escolha == 36:
        capital = float(input("Digite o capital inicial: "))
        taxa = float(input("Digite a taxa de juros (em decimal): "))
        tempo = float(input("Digite o tempo (em anos): "))
        print(f"Juros Simples: {juros_simples(capital, taxa, tempo)}")
    elif escolha == 37:
        capital = float(input("Digite o capital inicial: "))
        taxa = float(input("Digite a taxa de juros (em decimal): "))
        tempo = float(input("Digite o tempo (em anos): "))
        print(f"Juros Compostos: {juros_compostos(capital, taxa, tempo)}")
    elif escolha == 38:
        n = int(input("Digite o valor de n: "))
        print(f"Soma de Números Naturais: {soma_numeros_naturais(n)}")
    elif escolha == 39:
        n = int(input("Digite o valor de n: "))
        print(f"Fatorial de {n}: {fatorial(n)}")
    elif escolha == 40:
        n = int(input("Digite o valor de n: "))
        r = int(input("Digite o valor de r: "))
        print(f"Permutação de {n} e {r}: {permutacao(n, r)}")
    elif escolha == 41:
        n = int(input("Digite o valor de n: "))
        r = int(input("Digite o valor de r: "))
        print(f"Combinação de {n} e {r}: {combinacao(n, r)}")
    elif escolha == 42:
        numero = int(input("Digite o número a ser convertido: "))
        base = input("Digite a base para conversão (binario ou hexadecimal): ")
        print(f"Resultado da conversão: {conversor_bases(numero, base)}")
    elif escolha == 43:
        valores = ler_lista_numeros("Digite os valores separados por espaço: ")
        print(f"Média: {calculo_media(valores)}")
    elif escolha == 44:
        valores = ler_lista_numeros("Digite os valores separados  por espaço: ")
        print(f"Desvio Padrão: {calculo_desvio_padrao(valores)}")
    elif escolha == 45:
        a = float(input("Digite o coeficiente angular da reta: "))
        print(f"Tangente da Reta: {tangente_reta(a)}")
    elif escolha == 0:
        print("Saindo...")
        return False
    else:
        print("Escolha inválida. Tente novamente.")
    return True

def ler_dois_numeros(mensagem1="Digite o primeiro número: ", mensagem2="Digite o segundo número: "):
    a = float(input(mensagem1))
    b = float(input(mensagem2))
    return a, b

def ler_dois_inteiros(mensagem1="Digite o primeiro número inteiro: ", mensagem2="Digite o segundo número inteiro: "):
    a = int(input(mensagem1))
    b = int(input(mensagem2))
    return a, b

def ler_tres_numeros(mensagem1="Digite o primeiro número: ", mensagem2="Digite o segundo número: ", mensagem3="Digite o terceiro número: "):
    a = float(input(mensagem1))
    b = float(input(mensagem2))
    c = float(input(mensagem3))
    return a, b, c

def ler_quatro_numeros(mensagem1="Digite o primeiro número: ", mensagem2="Digite o segundo número: ", 
                       mensagem3="Digite o terceiro número: ", mensagem4="Digite o quarto número: "):
    a = float(input(mensagem1))
    b = float(input(mensagem2))
    c = float(input(mensagem3))
    d = float(input(mensagem4))
    return a, b, c, d

def ler_lista_numeros(mensagem="Digite os números separados por espaço: "):
    valores = input(mensagem).split()
    return [float(valor) for valor in valores]

def main():
    while True:
        exibir_menu()
        escolha = int(input("Digite o número da operação desejada: "))
        if not executar_operacao(escolha):
            break

if __name__ == "__main__":
    main()