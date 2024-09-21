def multiplica_matrizes(A, B):
    if len(A[0]) != len(B):
        raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

C = [[1, 2, 3], [4, 5, 6]]
D = [[7, 8], [9, 10], [11, 12]]
print(multiplica_matrizes(C, D))