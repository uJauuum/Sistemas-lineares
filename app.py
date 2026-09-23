import streamlit as st

st.title("Atividade Matematica computacional")

st.write("by: Otavio, Vitor, João e Erick")

# Escolher tamanho
n = st.number_input(
    "Escolha o tamanho do sistema:",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)

st.subheader("Digite os coeficientes")

# Criar campos para a matriz
matriz = []

for i in range(n):
    colunas = st.columns(n + 1)
    linha = []

    for j in range(n + 1):
        if j == n:
            nome = f"b{i+1}"
        else:
            nome = f"a{i+1}{j+1}"

        numero = colunas[j].number_input(
            nome,
            value=0.0,
            key=f"{i}_{j}"
        )

        linha.append(numero)

    matriz.append(linha)


# Botão para resolver
if st.button("🚀 Resolver sistema"):

    # Mostrar sistema original
    st.subheader("1️⃣ Sistema Original")

    for linha in matriz:
        texto = " + ".join(
            f"({linha[j]:.2f})x{j+1}"
            for j in range(n)
        )

        texto += f" = {linha[n]:.2f}"
        st.write(texto)

    # Fazer uma cópia da matriz
    A = [linha[:] for linha in matriz]

    # Escalonamento
    for i in range(n):

        # Procurar um pivô
        pivo = i

        while pivo < n and abs(A[pivo][i]) < 0.000001:
            pivo += 1

        if pivo == n:
            continue

        # Trocar linhas
        A[i], A[pivo] = A[pivo], A[i]

        # Eliminar números abaixo do pivô
        for k in range(i + 1, n):

            if A[i][i] == 0:
                continue

            fator = A[k][i] / A[i][i]

            for j in range(i, n + 1):
                A[k][j] = A[k][j] - fator * A[i][j]

    # Mostrar matriz escalonada
    st.subheader("2️⃣ Sistema Escalonado")

    for linha in A:
        st.write(
            " | ".join(f"{numero:.2f}" for numero in linha)
        )

    # Verificar se não existe solução
    sem_solucao = False

    for i in range(n):

        todos_zero = True

        for j in range(n):
            if abs(A[i][j]) > 0.000001:
                todos_zero = False

        if todos_zero and abs(A[i][n]) > 0.000001:
            sem_solucao = True

    if sem_solucao:

        st.error("❌ O sistema não possui solução.")

    else:

        # Substituição regressiva
        x = [0.0] * n
        infinitas = False

        for i in range(n - 1, -1, -1):

            if abs(A[i][i]) < 0.000001:
                infinitas = True
                break

            soma = 0

            for j in range(i + 1, n):
                soma += A[i][j] * x[j]

            x[i] = (A[i][n] - soma) / A[i][i]

        if infinitas:

            st.warning("⚠️ O sistema possui infinitas soluções.")

        else:

            st.subheader("3️⃣ Solução")

            for i in range(n):
                st.success(f"x{i+1} = {x[i]:.2f}")
