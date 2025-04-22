print("Bienvenido a Certifika!")

nota = float(input("Por favor, ingresa tu calificación para ver a qué descuento accedes: "))

if nota >= 6:
    print("Recibirás un descuento del 20%")
elif nota >= 5:
    print("Recibirás un descuento del 15%")
elif nota >= 4:
    print("Recibirás un descuento del 10%")
else:
    print("Te invitamos a seguir trabajando...")
