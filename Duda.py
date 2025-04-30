import random

print("Bievenido al game de vixo, ingresa 2 numeros")

n1 = int(input("Ingres el primero numero: "))
n2 = int(input("Ingresa el segundo numero: "))

numero_aleatorio = random.randint(n1, n2)

print (f"El numero es{numero_aleatorio}")

porcentaje = float(input("Ingrese el % que desea: "))

resultado = numero_aleatorio *(porcentaje/100)

print(f"Resultado {resultado}")

print("A continuación, elige si quieres sumar (1) o restar (2)")
operacion = int(input())

if operacion == 1:
   print(resultado+numero_aleatorio)
elif operacion == 2:
    print(resultado-numero_aleatorio)
else:
    print("Opcion no valdia.")    
