def escalona_matriz(A):
    m = [linha[:] for linha in A]
    n = len(m)

    for i in range(n):
        if m[i][i] == 0:
            for j in range(i + 1, n):
                if m[j][i] != 0:
                    m[i], m[j] = m[j], m[i]
                    break
        
        divisor = m[i][i]
        for k in range(i, len(m[0])):
            m[i][k] /= divisor
        
        for j in range(i + 1, n):
            fator = m[j][i]
            for k in range(i, len(m[0])):
                m[j][k] -= fator * m[i][k]
    
    return m

G = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
print(escalona_matriz(G))