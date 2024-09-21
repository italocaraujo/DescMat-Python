def subtrai_matrizes(A, B):
    # Verifica se as matrizes têm a mesma dimensão
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("As matrizes devem ter a mesma dimensão.")
    
    # Subtração elemento a elemento
    resultado = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A[0])):
            linha.append(A[i][j] - B[i][j])
        resultado.append(linha)
    
    return resultado

# Definição das matrizes A e B
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Exemplo de uso
print(subtrai_matrizes(A, B))