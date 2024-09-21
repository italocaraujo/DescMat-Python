# Função para calcular o determinante de uma matriz
def determinante_matriz(A):
    # Verificar se a matriz é quadrada
    if len(A) != len(A[0]):
        raise ValueError("A matriz deve ser quadrada.")
    
    # Caso base: matriz 1x1
    if len(A) == 1:
        return A[0][0]
    
    # Caso base: matriz 2x2
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    # Determinante de matriz maior que 2x2
    det = 0
    for c in range(len(A[0])):
        menor = [linha[:c] + linha[c+1:] for linha in A[1:]]  # Submatriz menor
        det += ((-1) ** c) * A[0][c] * determinante_matriz(menor)
    
    return det

# Função para calcular a inversa de uma matriz
def inversa_matriz(A):
    det = determinante_matriz(A)
    if det == 0:
        raise ValueError("A matriz não é inversível.")

    # Matriz de cofatores
    cofatores = []
    for r in range(len(A)):
        linha_cofator = []
        for c in range(len(A)):
            menor = [linha[:c] + linha[c+1:] for linha in (A[:r] + A[r+1:])]
            cofator = ((-1) ** (r + c)) * determinante_matriz(menor)
            linha_cofator.append(cofator)
        cofatores.append(linha_cofator)
    
    # Transpor a matriz de cofatores
    cofatores_transposta = transposta_matriz(cofatores)

    # Dividir cada elemento pelo determinante
    return [[cofatores_transposta[i][j] / det for j in range(len(cofatores_transposta))] for i in range(len(cofatores_transposta))]

# Função para transpor uma matriz
def transposta_matriz(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Exemplo de uso
F = [[4, 7], [2, 6]]
print(inversa_matriz(F))