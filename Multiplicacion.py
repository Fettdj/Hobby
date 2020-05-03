filas1 = int(input("Introduce el numero de filas de matriz 1:"))
colum1 = int(input("Introduce el numero de columnas de la matriz 1:"))
colum2 = int(input("Introduce el numero de columnas matriz 2: "))

#MULTIPLICACION DE UNA MATRIZ DE 2 FILAS Y 3 COLUMNAS - 2COLUMNAS Y 3 FILAS

#Matriz 1
A = []
for i in range (filas1):
    A.append([0]*colum1)
    print(A[i])

#CREAMOS LA MATRIZ 2
B = []
for i in range(colum1): #Declarando filas de la matriz B
    B.append([0]*colum2)
    print(B[i])

for i in range(filas1):
    for j in range(colum1):
        A[i][j] = float(input("Introduce el componente (%d, %d): " % (i, j)))

for i in range(filas1):
    print(A[i])

 #Cambiar valores de la matriz 2
for i in range(colum1): #Representan las filas
     for j in range(colum2):
         B[i][j] = float(input("Introduce el componente (%d, %d): "% (i,j)))

for i in range(colum1):
    print(B[i])

#Matriz Resultado
C = []
for i in range(filas1):
    C.append([0]*colum2)

for i in range(filas1):
    print(C[i])

#MULTIPLICACION 
for i in range(filas1):
    for j in range(colum2):
        for k in range (colum1):
            C[i][j] += A[i][k] * B[k][j]

#MAtriz final
for i in range(filas1):
    R = []
    for j in range(colum2):
        R.append(C[i][j])
    print(R)


