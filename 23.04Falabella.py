print("Bienvenido a Puntos Falabella\nPor favor, ingresa tu nombre y cantidad de puntos para conocer tus descuento: ")
nombre = input("Nombre: ")
puntos = int(input("Puntos: "))

if puntos >= 1000:
    print(f"Genial! {nombre} Estas en el nivel premium, tu descuento será del 25%")
elif puntos >= 500:
    print(f"Genial! {nombre} Estas en el nivel oro, tu descuento será del 10%")
elif puntos >= 250:
    print(f"Genial {nombre} Estas en el nivel bromce, podrás acceder a diferentes premios")
else:
    print("Te invitamo a seguir acumulando puntos")  
