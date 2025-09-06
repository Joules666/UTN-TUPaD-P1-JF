#Práctico 1: Estructuras secuenciales


#Actividad 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


#Actividad 2: Crear un programa que pida al usuario su nombre e imprima 
# por pantalla un saludo usando el nombre ingresado.
nombre=input("Favor de ingresar su nombre:")
print(f"Hola {nombre}!")


#Actividad 3: Crear un programa que pida al usuario su nombre, apellido, 
# edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
nombre=input("Ingresar su nombre:")
apellido=input("Ingresar apellido:")
edad=input("Ingresar edad:")
residencia=input("Ingresar su país de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#Actividad 4: Crear un programa que pida al usuario el radio de un círculo e 
# imprima por pantalla su área y su perímetro.
radio=int(input("Ingresar el radio elegido:"))
pi=3.14
area=pi*(radio**2)
perimetro=2*pi*radio
print(f"Para el radio = {radio}, el área del circulo es {area} unidades cuadradas y su perimetro es {perimetro} unidades lineales")


#Actividad 5: Crear un programa que pida al usuario una cantidad de 
# segundos e imprima por pantalla a cuántas horas equivale.
segundos=int(input("Ingrese una cantidad de segundos:"))
horas=segundos/3600
print(f"Los {segundos} segundos ingresados equivalen a {horas} horas")


#Actividad 6: Crear un programa que pida al usuario un número e 
# imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Por favor, ingresa un número: "))
print(f"\nTabla de multiplicar del {numero}:")
print(f"{1} x {numero} = {1 * numero}")
print(f"{2} x {numero} = {2 * numero}")
print(f"{3} x {numero} = {3 * numero}")
print(f"{4} x {numero} = {4 * numero}")
print(f"{5} x {numero} = {5 * numero}")
print(f"{6} x {numero} = {6 * numero}")
print(f"{7} x {numero} = {7 * numero}")
print(f"{8} x {numero} = {8 * numero}")
print(f"{9} x {numero} = {9 * numero}")
print(f"{10} x {numero} = {10 * numero}")


#Actividad 7: Crear un programa que pida al usuario dos números 
# enteros distintos del 0 y muestre por pantalla el resultado de 
# sumarlos, dividirlos, multiplicarlos y restarlos.
n1=int(input("Ingresar el primer número: "))
n2=int(input("Ingresar el segundo número: "))
print(f"El resultado de su suma es = {n1 + n2}")
print(f"El resultado de su división es = {n1 / n2}")
print(f"El resultado de su multiplicación de los números ingresados es: {n1 * n2}")
print(f"El resultado de su resta es: {n1 - n2}")


#Actividad 8: Crear un programa que pida al usuario su altura y su 
# peso e imprima por pantalla su índice de masa corporal.
peso=float(input("Ingresar su peso en Kg: "))
altura=float(input("Ingresar su altura expresada en metros : "))
print(f"Su Indice de Masa Corporal (IMC) es = {peso / altura**2}")


#Actividad 9: Crear un programa que pida al usuario una temperatura 
# en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
tc=float(input("Ingresar valor de temperatura en °C: "))
print(f"El equivalente de {tc}°C en °F es = {(9/5) * tc + 32}°F")


#Actividad 10: Crear un programa que pida al usuario 3 números e 
# imprima por pantalla el promedio de dichos números.
input("Favor de ingresar 3 números, presione Enter para continuar")
n1=int(input("Ingresar primer valor: "))
n2=int(input("Ingresar segundo valor: "))
n3=int(input("Ingresar tercer valor: "))
print(f"El promedio de los 3 valores ingresados es = {(n1 + n2 + n3) / 3}")