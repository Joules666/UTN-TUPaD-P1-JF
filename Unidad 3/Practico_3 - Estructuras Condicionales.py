#Actividad 1: Escribir un programa que solicite la edad del usuario. 
#             Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla 
#             que diga “Es mayor de edad”.
edad=int(input(f"Ingresar su edad: "))  
if edad > 18:
    print(f"Es mayor de edad")
print(" ") #Espaciador para resultados


#Actividad 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#             mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#             mensaje “Desaprobado”.
nota=int(input(f"Ingresar su nota: "))  
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
print(" ") #Espaciador para resultados


#Actividad 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#             número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#             contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#             operador de módulo (%) en Python para evaluar si un número es par o impar.
cifra=int(input("Ingresar un número: "))  
if cifra % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
print(" ") #Espaciador para resultados


#Actividad 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#             siguientes categorías pertenece:
#             ● Niño/a: menor de 12 años.
#             ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#             ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#             ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad<12:
	print("Es Niño/a")
elif edad>=12 and edad<18:
	print("Es Adolescente")
elif edad>=18 and edad<30:
	print("Es Adulto/a joven")
else:
	print("Adulto")
print("  ") #Separador de resultados


#Actividad 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#             (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#             pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#             pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#             de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#             como una lista o un string.

contrasenna = len(input("Ingrese su contraseña: "))
if contrasenna>=8 and contrasenna<=14:
	print("Ha ingresado una contraseña correcta")
else:
	print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("  ") #Separador de resultados


#Actividad 6: Escribir un programa que tome la lista numeros_aleatorios, 
#             calcule su moda, su mediana y su media y las compare para determinar si 
#             hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media_val = mean(numeros_aleatorios)
mediana_val = median(numeros_aleatorios)
moda_val = mode(numeros_aleatorios)
if media_val > mediana_val > moda_val:
    print("Sesgo positivo")
elif media_val < mediana_val < moda_val:
    print("Sesgo negativo")
elif media_val == mediana_val == moda_val:
    print("Sin sesgo")
else:
    print("Distribución no clasificada")
print("  ") #Separador de resultados


#Actividad 7: Escribir un programa que solicite una frase o palabra al usuario. 
#             Si el string ingresado termina con vocal, añadir un signo de exclamación 
#             al final e imprimir el string resultante por pantalla; en caso contrario, 
#             dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
    frase += "!"
print(frase)
print("  ") #Separador de resultados


#Actividad 8: Este programa solicita el nombre del usuario y una opción para transformarlo en
#             mayúsculas, minúsculas o con la primera letra en mayúscula.
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")


 #Actividad 9: Este programa solicita la magnitud de un terremoto y la clasifica según la escala de Richter.
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")



#Actividad 10: Este programa solicita el hemisferio, mes y día, y determina la estación del año.
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
if hemisferio == "N":
    print("Estación:", estacion_norte)
elif hemisferio == "S":
    print("Estación:", estacion_sur)
else:
    print("Hemisferio inválido")