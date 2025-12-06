n = 0
es_valido = False

while not es_valido:
    entrada = input("Ingrese un numero mayor a 3: ")
    if entrada.isdigit():
        n = int(entrada)
        if n >= 3:
            es_valido = True

matriz = []
for i in range(n):
    fila = [0] * n
    matriz.append(fila)

valor = 1
inicio_fila = 0
fin_fila = n - 1
inicio_col = 0
fin_col = n - 1
#Creacion de matriz
while valor <= n * n:
    for i in range(inicio_col, fin_col + 1):
        matriz[inicio_fila][i] = valor
        valor += 1
    inicio_fila += 1

    for i in range(inicio_fila, fin_fila + 1):
        matriz[i][fin_col] = valor
        valor += 1
    fin_col -= 1

    if inicio_fila <= fin_fila:
        for i in range(fin_col, inicio_col - 1, -1):
            matriz[fin_fila][i] = valor
            valor += 1
        fin_fila -= 1

    if inicio_col <= fin_col:
        for i in range(fin_fila, inicio_fila - 1, -1):
            matriz[i][inicio_col] = valor
            valor += 1
        inicio_col += 1

for fila in matriz:
    for numero in fila:
        print(f"{numero:4}", end="")
    print()