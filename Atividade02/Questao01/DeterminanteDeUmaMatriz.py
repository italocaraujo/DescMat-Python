def determinante_matriz(A):
    if len(A) != len(A[0]):
        raise ValueError("A matriz deve ser quadrada.")
    
    # Caso base: matriz 2x2
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0
    for c in range(len(A)):
        det += ((-1) ** c) * A[0][c] * determinante_matriz([linha[:c] + linha[c+1:] for linha in A[1:]])
    return det

E = [[1, 2], [3, 4]]
print(determinante_matriz(E))