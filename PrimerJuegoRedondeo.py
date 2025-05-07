import random
print("Bienvenido al Juego de Vixo, podrás adinivar el numero aleatorio?\nDebes ingresar un limite inferior y superior")
n1 = int(input("Ingresa tu primer numero: ")) #limite inferior
n2 = int(input("Ingresa tu segundo numero: "))#limite superior

numero_aleatorio = random.randint(n1, n2)
resultado = round(numero_aleatorio / 4) * 4

print("Tu numero aleatorio fue divido entre 4 y redondeado al multiplo de 4 mas cercano...! ")

#Primer intento
adivinar1 = int(input("Ingresa tu primer intento: "))
if adivinar1 == numero_aleatorio:
    print("Felicidades, adivinaste al primer intento!")
    exit()
else:
    pista = "mayor" if adivinar1 < numero_aleatorio else "menor"
    print(f"El numero es {pista}, intenta nuevamente!")

#Segundo intento
adivinar2 = int(input("Ingresa tu segundo intento: "))
if adivinar2 == numero_aleatorio:
    print("Feliciades, atinaste en el segundo intento!")
    exit()
else: 
     pista = "mayor" if adivinar1 < numero_aleatorio else "menor"
     print(f"El numero es {pista}, tienes una ultima oportunidad!")

#tercer intento
adivinar3 = int(input("Ingresa tu tercer intento: "))
if adivinar3 == numero_aleatorio:
       print("Feliciades, atinaste en el tercer intento!")
else:
     print(f"El numero era {numero_aleatorio}, juega nuevamente!")       
