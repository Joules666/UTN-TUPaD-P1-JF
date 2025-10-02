#TP 5 - Listas

# Actividad 1 - Crear una lista con las notas de 10 estudiantes.
notas = [7, 8, 9, 6, 5, 10, 4, 8, 7, 6]
for nota in notas:
    print(nota)
promedio = sum(notas) / len(notas)
print('Promedio:', promedio)
print('Nota más alta:', max(notas))
print('Nota más baja:', min(notas))


# Actividad 2 - Pedir al usuario que cargue 5 productos en una lista.
productos = []
for i in range(5):
    productos.append(input(f'Ingrese el producto {i+1}: '))
productos.sort()
print('Lista ordenada:', productos)
eliminar = input('¿Qué producto desea eliminar?: ')
if eliminar in productos:
    productos.remove(eliminar)
print('Lista actualizada:', productos)


# Actividad 3 - Generar una lista con 15 números enteros al azar entre 1 y 100.
import random

numeros_aleatorios = []
for i in range(15):
    numero = random.randint(1, 100)
    numeros_aleatorios.append(numero)

print("Lista de números aleatorios:")
print(numeros_aleatorios)


# Actividad 4 - Dada una lista con valores repetidos.
lista_repetidos = [1, 2, 2, 3, 4, 4, 5]
lista_sin_repetidos = list(set(lista_repetidos))
print('Lista sin repetidos:', lista_sin_repetidos)


# Actividad 5 - Lista con nombres de 8 estudiantes presentes en clase.
estudiantes = ['Ana', 'Luis', 'Carlos', 'Marta', 'Sofía', 'Juan', 'Lucía', 'Pedro']
accion = input('¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ')
nombre = input('Ingrese el nombre: ')
if accion == 'agregar':
    estudiantes.append(nombre)
elif accion == 'eliminar' and nombre in estudiantes:
    estudiantes.remove(nombre)
print('Lista actualizada:', estudiantes)


# Actividad 6 - Rotar los elementos de una lista una posición a la derecha.
numeros = [1, 2, 3, 4, 5, 6, 7]
numeros = [numeros[-1]] + numeros[:-1]
print('Lista rotada:', numeros)


# Actividad 7 - Matriz 7x2 con temperaturas mínimas y máximas.
# [min, max] por día
temperaturas = [
    [12, 22],  # Día 1
    [10, 25],  # Día 2
    [14, 20],  # Día 3
    [13, 23],  # Día 4
    [11, 21],  # Día 5
    [9, 26],   # Día 6
    [15, 24]   # Día 7
]

suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0

for i in range(7):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    
    suma_min += minima
    suma_max += maxima
    
    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1  # Día 1 a 7

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print("Promedio de temperaturas mínimas:", round(promedio_min, 2))
print("Promedio de temperaturas máximas:", round(promedio_max, 2))
print("Día con mayor amplitud térmica:", dia_mayor_amplitud)


# Actividad 8 - Matriz con notas de 5 estudiantes en 3 materias.
notas = [
    [7, 8, 9],  # Estudiante 1
    [6, 7, 8],  # Estudiante 2
    [9, 9, 10], # Estudiante 3
    [5, 6, 7],  # Estudiante 4
    [8, 7, 9]   # Estudiante 5
]

print("Promedios por estudiante:")
for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas[i][j]
    promedio = suma / 3
    print(f"Estudiante {i+1}: {round(promedio, 2)}")

print("\nPromedios por materia:")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio = suma / 5
    print(f"Materia {j+1}: {round(promedio, 2)}")



# Actividad 9 - Tablero de Ta-Te-Ti como lista de listas.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugador = "X"

for turno in range(9):
    print("Turno del jugador", jugador)
    
    # Mostrar tablero
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()
    print()
    
    # Ingreso de posición
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))
    
    # Verificar si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada. Intente de nuevo.")
        continue  # Repetir turno sin cambiar de jugador
    
    # Cambiar de jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

# Mostrar tablero final
print("Tablero final:")
for i in range(3):
    for j in range(3):
        print(tablero[i][j], end=" ")
    print()



# Actividad 10 - Matriz de ventas de 4 productos durante 7 días.
# Matriz de ventas: 4 productos x 7 días
ventas = [
    [10, 12, 8, 15, 9, 11, 13],  # Producto 1
    [7, 9, 10, 8, 6, 7, 9],      # Producto 2
    [14, 13, 12, 16, 15, 14, 13],# Producto 3
    [5, 6, 7, 5, 6, 5, 4]        # Producto 4
]

print("Total vendido por cada producto:")
for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    print(f"Producto {i+1}: {total_producto}")

# Día con mayores ventas totales
mayor_ventas_dia = 0
dia_mayor_ventas = 0

for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    if total_dia > mayor_ventas_dia:
        mayor_ventas_dia = total_dia
        dia_mayor_ventas = j + 1  # Día 1 a 7

print("\nDía con mayores ventas totales:", dia_mayor_ventas)

# Indicar el producto más vendido en la semana
mayor_ventas_producto = 0
producto_mas_vendido = 0

for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    if total_producto > mayor_ventas_producto:
        mayor_ventas_producto = total_producto
        producto_mas_vendido = i + 1

print("Producto más vendido en la semana:", producto_mas_vendido)

