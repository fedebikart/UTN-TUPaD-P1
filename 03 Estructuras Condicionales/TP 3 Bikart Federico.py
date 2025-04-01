Ejercicio 1 
edad = int (input("Ingrese su edad: "))

if edad > 18:
    print ("Es mayor de edad")
else:
    print ("Es menor de edad")

Ejercicio 2
nota = int (input("Ingrese su nota: "))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

Ejercicio 3
pares = int (input("Ingrese un numero par: "))

if pares % 2 == 0:
    print ("Ha ingresado un numero par")
else:
    print ("Ha ingresado un numero impar")

Ejercicio 4
edad = int (input("Ingrese su edad: "))

if edad < 12:
    print ("Usted es un niño/a")
elif edad >= 12 and edad < 18:
    print ("Usted es un adolescente")
elif edad >= 18 and edad < 30:
    print ("Usted es un adulto/a joven")
elif edad >= 30:
    print ("Usted es un adulto/a")

Ejercicio 5
contraseña = (input("Ingrese una contraseña: "))
if 8 <= len (contraseña) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

Ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
print(f"Resultado: {sesgo}")

Ejercicio 7
frase_palabra = (input("Ingrese una palabra o frase: "))

vocales = "aeiouAEIOU"

if frase_palabra [-1] in vocales:
    print (f"{frase_palabra} !")
else:
    print (frase_palabra)

Ejercicio 8
nombre = (input ("Ingrese su nombre: "))
opcion = int(input("Ingresa el número de la opción que deseas:\n1. Mayúsculas\n2. Minúsculas\n3. Primer letra mayúscula\n"))

if opcion == 1:
    print (nombre.upper())
elif opcion == 2:
    print (nombre.lower())
elif opcion == 3:
    print (nombre.title())

Ejercicio 9
terremoto = float (input("Ingrese la magnitud de un terremoto: "))
if terremoto < 3:
    print ("Muy leve (Imperceptible)")
elif terremoto >= 3 and terremoto < 4:
    print ("Leve (Ligeramente perceptible)")
elif terremoto >= 4 and terremoto < 5:
    print ("Moderado (Sentido por personas, pero generalmente no causa daños)")
elif terremoto >= 5 and terremoto < 6:
    print ("Fuerte (Puede causar daños en estructuras debiles)")
elif terremoto >= 6 and terremoto < 7:
    print ("Muy fuerte (Puede causar daños significativos)")
elif terremoto >= 7:
    print ("Extremo (Puede causar graves daños a gran escala)")

Ejercicio 10
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()  
mes = int(input("¿Qué mes del año es? (1-12): "))  
dia = int(input("¿Qué día es hoy? (1-31): "))  

if hemisferio == "N":  
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):  
        print("Invierno")  
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):  
        print("Primavera")  
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):  
        print("Verano")  
    else:  
        print("Otoño")  

elif hemisferio == "S":  
    if (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):  
        print("Invierno")  
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):  
        print("Primavera")  
    elif (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):  
        print("Verano")  
    else:  
        print("Otoño")  


