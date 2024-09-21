import math

def menu():
    print("Bem-vindo a Calculadora!")
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtracao")
    print("3. Multiplicacao")
    print("4. Divisao")
    print("5. Potenciacao")
    print("6. Radiciacao")
    print("7. Exponencial")
    print("8. Modulo")
    print("9. Divisao Inteira")
    print("10. Graus para Radianos")
    print("11. Radianos para Graus")
    print("12. Calculo de Hipotenusa")
    print("13. Arredondamento")
    print("14. Arredondamento para Cima")
    print("15. Arredondamento para Baixo")
    print("16. Maior/Menor de Dois Numeros")
    print("17. Distancia Entre Dois Pontos")
    print("18. Determinante de Matriz 2x2")
    print("19. Solucao de Equacao de Primeiro Grau")
    print("0. Sair")

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b if b != 0 else "Erro: Divisao por zero"

def potencia(a, b):
    return a ** b

def radiciacao(a, n=2):
    return a ** (1/n)

def exponencial(x):
    return math.exp(x)

def modulo(a, b):
    return abs(a)

def divisao_inteira(a, b):
    return a // b

def graus_para_radianos(graus):
    return math.radians(graus)

def radianos_para_graus(radianos):
    return math.degrees(radianos)

def calculo_hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

def arredondamento(a):
    return round(a)

def arredondamento_cima(a):
    return math.ceil(a)

def arredondamento_baixo(a):
    return math.floor(a)

def maior(a, b):
    return max(a, b)

def menor(a, b):
    return min(a, b)

def distancia_entre_pontos(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def determinante_matriz_2x2(a, b, c, d):
    return a * d - b * c

def solucao_equacao_primeiro_grau(a, b):
    return -b / a if a != 0 else "Erro: Coeficiente a nao pode ser zero"

# Loop principal da calculadora
while True:
    menu()
    opcao = int(input("Digite sua opcao: "))
    
    if opcao == 0:
        print("Saindo...")
        break

    if opcao in range(1, 20):
        if opcao in [1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16]:
            a = float(input("Digite o primeiro numero: "))
            b = float(input("Digite o segundo numero: "))
            if opcao == 1:
                print(f"Resultado: {soma(a, b)}")
            elif opcao == 2:
                print(f"Resultado: {subtracao(a, b)}")
            elif opcao == 3:
                print(f"Resultado: {multiplicacao(a, b)}")
            elif opcao == 4:
                print(f"Resultado: {divisao(a, b)}")
            elif opcao == 5:
                print(f"Resultado: {potencia(a, b)}")
            elif opcao == 8:
                print(f"Resultado: {modulo(a)}")
            elif opcao == 9:
                print(f"Resultado: {divisao_inteira(a, b)}")
            elif opcao == 12:
                print(f"Resultado: {calculo_hipotenusa(a, b)}")
            elif opcao == 13:
                print(f"Resultado: {arredondamento(a)}")
            elif opcao == 14:
                print(f"Resultado: {arredondamento_cima(a)}")
            elif opcao == 15:
                print(f"Resultado: {arredondamento_baixo(a)}")
            elif opcao == 16:
                print(f"Maior: {maior(a, b)}, Menor: {menor(a, b)}")

        elif opcao in [6, 7, 10, 11, 17, 18, 19]:
            if opcao == 6:
                a = float(input("Digite o numero: "))
                n = int(input("Digite a raiz (2 para raiz quadrada, 3 para cúbica, etc.): "))
                print(f"Resultado: {radiciacao(a, n)}")
            elif opcao == 7:
                x = float(input("Digite o valor de x: "))
                print(f"Resultado: {exponencial(x)}")
            elif opcao == 10:
                graus = float(input("Digite os graus: "))
                print(f"Resultado: {graus_para_radianos(graus)} radianos")
            elif opcao == 11:
                radianos = float(input("Digite os radianos: "))
                print(f"Resultado: {radianos_para_graus(radianos)} graus")
            elif opcao == 17:
                x1 = float(input("Digite x1: "))
                y1 = float(input("Digite y1: "))
                x2 = float(input("Digite x2: "))
                y2 = float(input("Digite y2: "))
                print(f"Resultado: {distancia_entre_pontos(x1, y1, x2, y2)}")
            elif opcao == 18:
                a = float(input("Digite a: "))
                b = float(input("Digite b: "))
                c = float(input("Digite c: "))
                d = float(input("Digite d: "))
                print(f"Resultado: {determinante_matriz_2x2(a, b, c, d)}")
            elif opcao == 19:
                a = float(input("Digite o coeficiente a: "))
                b = float(input("Digite o coeficiente b: "))
                print(f"Resultado: {solucao_equacao_primeiro_grau(a, b)}")

        else:
            print("Opcao invalida.")

    else:
        print("Opcao fora do intervalo.")