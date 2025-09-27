#TP 5 - Listas

# Actividad 1: Crear una lista con los números del 1 al 10 e imprimirla.
lista = list(range(1, 11))
print("Lista del 1 al 10:", lista)

# Actividad 2: Crear una lista con los números pares del 2 al 20 e imprimirla.
pares = list(range(2, 21, 2))
print("Números pares del 2 al 20:", pares)

# Actividad 3: Dada la lista [3, 7, 1, 4, 9], imprimir el mayor y el menor valor.
numeros = [3, 7, 1, 4, 9]
print("Mayor:", max(numeros))
print("Menor:", min(numeros))

# Actividad 4: Dada la lista [5, 8, 2, 9, 1], ordenar la lista e imprimirla.
lista = [5, 8, 2, 9, 1]
lista.sort()
print("Lista ordenada:", lista)

# Actividad 5: Dada la lista [10, 20, 30, 40, 50], imprimir el segundo y el penúltimo elemento.
lista = [10, 20, 30, 40, 50]
print("Segundo elemento:", lista[1])
print("Penúltimo elemento:", lista[-2])

# Actividad 6: Dada la lista [1, 2, 3, 4, 5], agregar el número 6 al final e imprimirla.
lista = [1, 2, 3, 4, 5]
lista.append(6)
print("Lista con 6 agregado:", lista)

# Actividad 7: Dada la lista [1, 2, 3, 4, 5], eliminar el número 3 e imprimirla.
lista = [1, 2, 3, 4, 5]
lista.remove(3)
print("Lista sin el 3:", lista)

# Actividad 8: Dada la lista [1, 2, 3, 4, 5], insertar el número 10 en la posición 2 e imprimirla.
lista = [1, 2, 3, 4, 5]
lista.insert(2, 10)
print("Lista con 10 en posición 2:", lista)

# Actividad 9: Dada la lista [1, 2, 3, 4, 5], imprimir los elementos en orden inverso.
lista = [1, 2, 3, 4, 5]
print("Lista invertida:", lista[::-1])

# Actividad 10: Dada la lista [1, 2, 3, 4, 5], imprimir la suma de sus elementos.
lista = [1, 2, 3, 4, 5]
print("Suma de elementos:", sum(lista))
