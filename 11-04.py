print("Bienvenido a supermercados El Vicho")
print("¿Que productos desea comprar el dia de hoy? Ingreselos a continuacion: ")

producto1=input(print("Añade el primer producto"))
producto2=input(print("Añade tu segundo producto"))
producto3=input(print("Añade tu tercer producto"))
producto4=input(print("Añade tu cuarto producto"))

lista=producto1, producto2, producto3, producto4,
print("Tus productos son", lista)
print("¿Desea agregar otro producto?")

agregar=input(print("Cual desea agregar?: "))

lista=agregar, producto1, producto2, producto3, producto4

print("Entonces serían: ", lista)

