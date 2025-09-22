#Actividad 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#             (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
num=0
while num<=100:
    print(f"{num}")
    num+=1
print("     ")   


#Actividad 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#             dígitos que contiene.
numero=input("Ingrese un numero entero: ")
digito=0
cont=0
for digito in numero:
    cont+=1
print(f"El número ingresado contiene {cont} cifras")   
print("     ")


#Actividad 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#             dados por el usuario, excluyendo esos dos valores.
val1=int(input("Ingrese el número que hará de límite inferior: "))
val2=int(input("Ingrese el número que hará de límite superior: "))
numero=val1+1
sumatoria=0
while val1<numero<val2:
    sumatoria+=numero
    numero+=1
print(f"La suma de los número contenidos entre {val1} y {val2} es igual a {sumatoria}")
print("       ")


#Actividad 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en
#             secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#             un 0.
num=int(input("Ingrese un número para iniciar la suma: "))
sumatoria=0
while num!=0: 
    sumatoria+=num
    num=int(input("Ingrese otro número para sumar: "))
print(f"La suma total de los números ingresados es: {sumatoria}")
print("         ")


#Actividad 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#             debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
aleat = random.randint(0, 9)
num=int(input("Ingrese un número del 0 al 9 y pruebe su suerte: "))
while num != aleat:
    num=int(input("Ingrese otro número del 0 al 9 y pruebe su suerte: "))
print(f"!!Adivinaste!! El número con el que acertaste es el {num}")
print("         ")


#Actividad 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#             entre 0 y 100, en orden decreciente.
num=100
while num>=0:
    print(num)
    num-=2
print("         ")


#Actividad 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#             número entero positivo indicado por el usuario.
num_sup=int(input("Ingrese su limite superior: "))
sumatoria=0
for i in range (0, num_sup):
    sumatoria+=i
    #print(sumatoria)
print(f"La suma total de los números entre 0 y {num_sup} es: {sumatoria}")
print("         ")


#Actividad 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#             programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#             negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#             menor, pero debe estar preparado para procesar 100 números con un solo cambio).
contpar=0
contimp=0
contneg=0
contpos=0
for i in range(0,100):
    num=int(input("Ingrese un número= "))
    if num % 2==0:
        contpar+=1
    else:
        contimp+=1
    if num>0:
        contpos+=1
    elif num<0:
        contneg+=1
mensaje=f"Del total de 100 números ingresados: \n{contpar} son pares\n{contimp} son impares\n{contpos} son positivos\n{contneg} son negativos"        
print(mensaje)
print("         ")


#Actividad 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#             media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#             poder procesar 100 números cambiando solo un valor).
num=0
sumatoria=0
contnum=0
media=0
for i in range(0,10):
    num=int(input("Ingrese un número= "))
    sumatoria+=num
    contnum+=1
media=sumatoria/contnum
print(f"La media de los 100 valores ingresados es: {media}")
print("         ")


#Actividad 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#              usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
num=(input("Ingrese un número= "))

mun=" "
for i in range(len(num)-1,-1,-1):
    mun += num[i]   
print(f"{mun}")