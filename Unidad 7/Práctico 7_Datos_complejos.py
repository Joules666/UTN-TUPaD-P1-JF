"""
Práctico 7: Estructuras de datos complejas
"""

# Ejercicio 1:
# Dado el diccionario precios_frutas:
#    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#    Añadir las siguientes frutas con sus respectivos precios:
#       • Naranja = 1200
#       • Manzana = 1500
#       • Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregamos las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario de precios de frutas (con nuevas frutas agregadas):")
print(precios_frutas)
print()


# Ejercicio 2:
#    Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar
#    el código desarrollado en el punto anterior, actualizar los precios de las
#    siguientes frutas:
#       • Banana = 1330
#       • Manzana = 1700
#       • Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Actualizamos los precios indicados
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario de precios de frutas (con precios actualizados):")
print(precios_frutas)
print()


# Ejercicio 3:
#    Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar
#    el código desarrollado en el punto anterior, crear una lista que contenga
#    únicamente las frutas sin los precios.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Obtenemos solo las claves (nombres de frutas)
lista_frutas = list(precios_frutas.keys())

print("Lista de frutas sin precios:")
print(lista_frutas)
print()


# Ejercicio 4:
#    Escribí un programa que permita almacenar y consultar números telefónicos.
#    • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#    • Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda_telefonos = {}

# Carga de 5 contactos
for i in range(5):
    print(f"Carga de contacto {i + 1}/5")
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    agenda_telefonos[nombre] = numero

print("\nAgenda cargada:")
print(agenda_telefonos)

# Consulta de un contacto
nombre_buscar = input("\nIngrese el nombre del contacto a buscar: ")
if nombre_buscar in agenda_telefonos:
    print(f"El número de {nombre_buscar} es: {agenda_telefonos[nombre_buscar]}")
else:
    print(f"No se encontró el contacto '{nombre_buscar}' en la agenda.")
print()


# Ejercicio 5:
#    Solicita al usuario una frase e imprime:
#    • Las palabras únicas (usando un set).
#    • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

# Normalizamos la frase a minúsculas y la separamos en palabras
palabras = frase.lower().split()

# Palabras únicas usando un set
palabras_unicas = set(palabras)

# Contador de apariciones usando un diccionario
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("\nPalabras únicas (set):")
print(palabras_unicas)

print("\nCantidad de apariciones de cada palabra:")
print(contador_palabras)
print()


# Ejercicio 6:
#    Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#    Luego, mostrá el promedio de cada alumno.

alumnos = {}

# Cargamos 3 alumnos con una tupla de 3 notas cada uno
for i in range(3):
    print(f"Carga de datos del alumno {i + 1}/3")
    nombre_alumno = input("Ingrese el nombre del alumno: ")

    # Cargamos 3 notas
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} de {nombre_alumno}: "))
        notas.append(nota)

    # Convertimos la lista de notas en tupla y la guardamos
    alumnos[nombre_alumno] = tuple(notas)
    print()

# Mostramos el promedio de cada alumno
print("Promedios de los alumnos:")
for nombre_alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre_alumno}: notas {notas} -> promedio = {promedio:.2f}")
print()


# Ejercicio 7:
#    Dados dos sets de números, representando dos listas de estudiantes que
#    aprobaron Parcial 1 y Parcial 2:
#       • Mostrá los que aprobaron ambos parciales.
#       • Mostrá los que aprobaron solo uno de los dos.
#       • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Ejemplo de sets de estudiantes (pueden modificarse según se necesite)
aprob_parcial1 = {1, 2, 3, 4, 5}
aprob_parcial2 = {4, 5, 6, 7}

print(f"Estudiantes que aprobaron Parcial 1: {aprob_parcial1}")
print(f"Estudiantes que aprobaron Parcial 2: {aprob_parcial2}")

# Estudiantes que aprobaron ambos parciales
ambos = aprob_parcial1 & aprob_parcial2

# Estudiantes que aprobaron solo uno de los dos parciales
solo_uno = (aprob_parcial1 ^ aprob_parcial2)

# Estudiantes que aprobaron al menos un parcial
al_menos_uno = aprob_parcial1 | aprob_parcial2

print(f"Estudiantes que aprobaron ambos parciales: {ambos}")
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {solo_uno}")
print(f"Estudiantes que aprobaron al menos un parcial (sin repetir): {al_menos_uno}")
print()


# Ejercicio 8
#    Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#    Permití al usuario:
#       • Consultar el stock de un producto ingresado.
#       • Agregar unidades al stock si el producto ya existe.
#       • Agregar un nuevo producto si no existe.

stock_productos = {
    "lapicera": 10,
    "cuaderno": 5,
    "goma": 20
}

print("Stock inicial de productos:")
print(stock_productos)

producto = input("\nIngrese el nombre del producto a consultar o actualizar: ").lower()

if producto in stock_productos:
    print(f"El stock actual de '{producto}' es: {stock_productos[producto]} unidades.")
    agregar_texto = input("¿Cuántas unidades desea agregar al stock? (ingrese 0 si no desea agregar): ")

    # Validamos que la entrada sea un número entero no negativo
    if agregar_texto.isdigit():
        agregar = int(agregar_texto)
        if agregar > 0:
            stock_productos[producto] += agregar
            print(f"Nuevo stock de '{producto}': {stock_productos[producto]} unidades.")
        else:
            print("No se agregaron unidades.")
    else:
        print("No se ingresó un número válido. No se realizaron cambios en el stock.")
else:
    print(f"El producto '{producto}' no existe en el stock.")
    respuesta = input("¿Desea agregar este nuevo producto? (s/n): ").lower()
    if respuesta == "s":
        unidades_texto = input("Ingrese la cantidad inicial de unidades: ")

        # Validamos que la entrada sea un número entero no negativo
        if unidades_texto.isdigit():
            unidades = int(unidades_texto)
            stock_productos[producto] = unidades
            print(f"Producto '{producto}' agregado con {unidades} unidades.")
        else:
            print("Cantidad inválida. No se agregó el producto.")
    else:
        print("No se agregó el producto.")

print("\nStock final:")
print(stock_productos)
print()


# Ejercicio 9:
#    Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#    Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "09:00"): "Reunión de trabajo",
    ("lunes", "15:00"): "Clase de Programación",
    ("martes", "10:30"): "Turno médico",
    ("miércoles", "18:00"): "Gimnasio"
}

print("Agenda de ejemplo:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia.title()} a las {hora}: {evento}")

dia_consulta = input("\nIngrese el día a consultar (por ejemplo, lunes): ").lower()
hora_consulta = input("Ingrese la hora a consultar (formato HH:MM): ")

clave_consulta = (dia_consulta, hora_consulta)

if clave_consulta in agenda:
    print(f"La actividad para {dia_consulta.title()} a las {hora_consulta} es: {agenda[clave_consulta]}")
else:
    print(f"No hay actividades registradas para {dia_consulta.title()} a las {hora_consulta}.")
print()


# Ejercicio 10:
#     Dado un diccionario que mapea nombres de países con sus capitales,
#     construí un nuevo diccionario donde:
#        • Las capitales sean las claves.
#        • Los países sean los valores.

paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Chile": "Santiago",
    "Paraguay": "Asunción"
}

print("Diccionario original (país -> capital):")
print(paises_a_capitales)

# Invertimos el diccionario: capital -> país
capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}

print("\nDiccionario invertido (capital -> país):")
print(capitales_a_paises)
print()
