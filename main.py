from solver import resolver


def mostrar_matriz(matriz):
    for linha in matriz:
        print(" | ".join(f"{numero:.2f}" for numero in linha))


print("=" * 45)
print("     ATIVIDADE MATEMÁTICA COMPUTACIONAL")
print("=" * 45)

print("\nDigite o tamanho do sistema.")
n = int(input("Tamanho: "))

matriz = []

print("\nDigite os coeficientes:")

for i in range(n):
    linha = []

    print(f"\nEquação {i + 1}")

    for j in range(n):
        valor = float(input(f"a{i + 1}{j + 1}: "))
        linha.append(valor)

    b = float(input(f"b{i + 1}: "))
    linha.append(b)

    matriz.append(linha)


print("\n1. Sistema Original")
mostrar_matriz(matriz)

status, x, escalonada = resolver(matriz)

print("\n2. Sistema Escalonado")
mostrar_matriz(escalonada)

if status == "sem_solucao":

    print("\nO sistema não possui solução.")

elif status == "infinitas":

    print("\nO sistema possui infinitas soluções.")

else:

    print("\n3. Solução")

    for i in range(n):
        print(f"x{i + 1} = {x[i]:.2f}")
