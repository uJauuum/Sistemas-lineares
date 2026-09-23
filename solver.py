def escalonar(matriz):
    n = len(matriz)
    A = [linha[:] for linha in matriz]

    for i in range(n):
        pivo = i

        while pivo < n and abs(A[pivo][i]) < 0.000001:
            pivo += 1

        if pivo == n:
            continue

        A[i], A[pivo] = A[pivo], A[i]

        for k in range(i + 1, n):
            if abs(A[i][i]) < 0.000001:
                continue

            fator = A[k][i] / A[i][i]

            for j in range(i, n + 1):
                A[k][j] -= fator * A[i][j]

    return A


def resolver(matriz):
    n = len(matriz)
    A = escalonar(matriz)

    # Verificar sistema impossível
    for i in range(n):
        todos_zero = all(abs(A[i][j]) < 0.000001 for j in range(n))

        if todos_zero and abs(A[i][n]) > 0.000001:
            return "sem_solucao", None, A

    # Verificar infinitas soluções
    for i in range(n):
        if abs(A[i][i]) < 0.000001:
            return "infinitas", None, A

    # Substituição regressiva
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        soma = 0

        for j in range(i + 1, n):
            soma += A[i][j] * x[j]

        x[i] = (A[i][n] - soma) / A[i][i]

    return "unica", x, A
