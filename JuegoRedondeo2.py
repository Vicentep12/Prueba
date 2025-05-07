import random   
print("Bienvenido al programa de vixo!\nLograrás adivinar el numero en 3 intentos?...")
print("Por favor, a continuacion ingresa 2 numeros enteros, uno menor y otro mayor")

n1 = int(input("Ingresa tu primer numero: "))
n2 = int(input("Ingresa tu segundo numero: "))

numero_aleatorio = random.randint(n1, n2)

#Adinivar!!!

adivinar1 = int(input("Ingresa tu primer intento: "))
if adivinar1 == numero_aleatorio:
    print("Adivinaste en el primer intento!")
    exit()
else: 
    pista = "mayor" if adivinar1 < numero_aleatorio else "menor" 
    print(f"Erraste, tu numero es {pista}") 

adivinar2 = int(input("Ingresa tu segundo intento: "))
if adivinar2 == numero_aleatorio:
    print("Felicidades, adivinaste en el segundo intento!!")
    exit()
else: 
     pista = "mayor" if adivinar1 < numero_aleatorio else "menor" 
     print(f"Erraste, tu numero es {pista}. Te queda un ultimo intento")  

adivinar3 = int(input("Ingresa tu ultimo intento!"))
if adivinar3 == numero_aleatorio:
    print("Adivinaste en tu ultimo intento!! ")
else:
    print(f"El nuermo era {numero_aleatorio}, suerte para la proxima!")

