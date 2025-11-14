"""
TP 7 - Recursividad
"""


# Ejercicio 1
# Crea una función recursiva que calcule el factorial de un número.
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial
# de todos los números enteros entre 1 y el número que indique el usuario.

def factorial(n):
    """Calcula el factorial de n de forma recursiva.
    Se asume n entero mayor o igual que 0.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def ejercicio_1():
    print("\n- Factorial recursivo -")
    numero = int(input("Ingrese un número entero positivo: "))
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")



# Ejercicio 2
# Crea una función recursiva que calcule el valor de la serie de Fibonacci
# en la posición indicada. Posteriormente, muestra la serie completa hasta la
# posición que el usuario especifique.

def fibonacci(pos):
    """Devuelve el valor de Fibonacci en la posición pos (0, 1, 2, ...).
    Definición:
        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2) para n >= 2
    """
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)


def ejercicio_2():
    print("\n-Serie de Fibonacci recursiva -")
    posicion = int(input("Ingrese la posición máxima (entero >= 0): "))
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(fibonacci(i), end=" ")
    print()  # salto de línea



# Ejercicio 3
# Crea una función recursiva que calcule la potencia de un número base elevado
# a un exponente, utilizando la fórmula n^m = n * n^(m-1).
# Prueba esta función en un algoritmo general.


def potencia(base, exponente):
    """Calcula base**exponente recursivamente.
    Se asume exponente entero mayor o igual que 0.
    """
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


def ejercicio_3():
    print("\n- Potencia recursiva -")
    base = int(input("Ingrese la base (entero): "))
    exponente = int(input("Ingrese el exponente (entero >= 0): "))
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es {resultado}")



# Ejercicio 4
# Crear una función recursiva en Python que reciba un número entero positivo
# en base decimal y devuelva su representación en binario como una cadena
# de texto.


def decimal_a_binario(n):
    """Convierte un número entero positivo n a su representación binaria
    usando recursividad. Devuelve una cadena de texto.
    """
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)


def ejercicio_4():
    print("\n- Conversión decimal a binario recursiva -")
    numero = int(input("Ingrese un número entero positivo: "))
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es {binario}")



# Ejercicio 5
# Implementá una función recursiva llamada es_palindromo(palabra) que reciba
# una cadena de texto sin espacios ni tildes, y devuelva True si es un
# palíndromo o False si no lo es.
#
# Requisitos:
#   - La solución debe ser recursiva.
#   - No se debe usar [::-1] ni la función reversed().


def es_palindromo(palabra):
    """Determina de forma recursiva si 'palabra' es un palíndromo."""
    # Caso base: cadenas de 0 o 1 carácter siempre son palíndromos
    if len(palabra) <= 1:
        return True
    # Si el primer y último carácter son distintos, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la subcadena sin el primero ni el último carácter
    return es_palindromo(palabra[1:-1])


def ejercicio_5():
    print("\n- Verificación de palíndromo recursivo -")
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    if es_palindromo(palabra):
        print(f"'{palabra}' ES un palíndromo.")
    else:
        print(f"'{palabra}' NO es un palíndromo.")



# Ejercicio 6
# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba
# un número entero positivo y devuelva la suma de todos sus dígitos.
#
# Restricciones:
#   - No se puede convertir el número a string.
#   - Usar operaciones matemáticas (%, //) y recursión.


def suma_digitos(n):
    """Suma recursivamente los dígitos de un número entero positivo n,
    sin convertirlo a cadena.
    """
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


def ejercicio_6():
    print("\n- Suma de dígitos recursiva -")
    numero = int(input("Ingrese un número entero positivo: "))
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es {resultado}")



# Ejercicio 7
# Un niño está construyendo una pirámide con bloques. En el nivel más bajo
# coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente
# hasta llegar al último nivel con un solo bloque.
#
# Escribí una función recursiva contar_bloques(n) que reciba el número de
# bloques en el nivel más bajo y devuelva el total de bloques que necesita
# para construir toda la pirámide.


def contar_bloques(n):
    """Devuelve recursivamente el total de bloques necesarios para construir
    una pirámide donde el nivel más bajo tiene n bloques, el siguiente n-1,
    y así sucesivamente hasta 1.
    """
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


def ejercicio_7():
    print("\n- Pirámide de bloques recursiva -")
    niveles = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
    total = contar_bloques(niveles)
    print(f"Para una pirámide con {niveles} bloques en el nivel más bajo se necesitan {total} bloques en total.")



# Ejercicio 8
# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba
# un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva
# cuántas veces aparece ese dígito dentro del número.


def contar_digito(numero, digito):
    """Cuenta recursivamente cuántas veces 'digito' aparece en 'numero'.
    Se asume que numero es un entero positivo y digito es un entero entre 0 y 9.
    """
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    return contar_digito(resto, digito)


def ejercicio_8():
    print("\n- Contar dígitos recursivo -")
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito entre 0 y 9: "))
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} vez/veces en el número {numero}.")



# Programa principal con menú para probar cada ejercicio


def mostrar_menu():
    print("\n================ MENÚ PRINCIPAL =================")
    print("1 - Ejercicio 1: Factoriales")
    print("2 - Ejercicio 2: Serie de Fibonacci")
    print("3 - Ejercicio 3: Potencia")
    print("4 - Ejercicio 4: Decimal a binario")
    print("5 - Ejercicio 5: Palíndromo")
    print("6 - Ejercicio 6: Suma de dígitos")
    print("7 - Ejercicio 7: Pirámide de bloques")
    print("8 - Ejercicio 8: Contar dígito en número")
    print("9 - Salir")
    print("=================================================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7()
        elif opcion == "8":
            ejercicio_8()
        elif opcion == "9":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
