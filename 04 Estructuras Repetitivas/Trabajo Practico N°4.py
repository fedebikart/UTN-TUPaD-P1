Ejercicio 1 
for x in range (0,101):
    print (x)

Ejercicio 2
numero = int(input("Ingrese un numero entero: "))
cant_digitos = (len(str(abs(numero))))
print ("Cantidad de digitos", cant_digitos)

Ejercicio 3 
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

menor = min(num1,num2)
mayor = max(num1,num2)
suma = 0

for x in range (menor + 1, mayor):
    suma += x
print ("La suma entre los dos numeros es de: ", suma)

Ejercicio 4
total = 0
num = int(input("Ingrese un numero (0 Para terminar): "))
while num != 0:
    total += num
    num = int(input("Ingrese un numero (0 para terminar): "))
print ("La suma total es: ", total)

Ejercicio 5 
import random
secreto = random.randint (0,9)
intentos = 0
adivina = -1

while adivina != secreto:
    adivina = (int(input("Adivina el numero entre 0 y 9: ")))
    intentos += 1
print ("Correcto, lo adivinaste en:", intentos, "intento(s)")

Ejercicio 6
for x in range (100, -1, -2):
    print ((x), " ",end="")

Ejercicio 7
limite = int(input("Ingrese un numero entero positivo: "))
suma = 0
for x in range (0, limite + 1):
    suma += x
print ("La suma es: ", suma)

Ejercicio 8
num_pares = 0
num_impares = 0
num_negativos = 0
num_positivos = 0

cantidad = int(input("Ingrese 100 numeros enteros: "))
for i in range (100):
    num = int(input(f"Numero {i+1}: "))
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares +=1
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativo += 1
print ("Pares: ", num_pares)
print ("Impares: ", num_impares)
print ("Positivos: ", num_positivos)
print ("Negativos: ", num_negativos)

Ejercicio 9
total = 0 
for i in range(100):
    num = int(input(f"Número {i+1}: "))
    total += num
media = total / 100

print ("La media es: ", media)

Ejercicio 10
numero = input("Ingresa un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)

