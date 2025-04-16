
print("Bienvenido al menú de opciones.")
print("Por favor selecciona la opcion que desees")

print("1.-Saludo")
print("2.-Despedida")
print("3.-Edad")
print("4.-Opcion invalida")

opcion=int(input("Selecciona una opcion entre 1-4: "))

if opcion == 1:
    print("Bienvenido amigazo")
elif opcion == 2: 
    print("Largaros de aqui")
elif opcion == 3:
    input(print("Indicame tu edad: "))
else:
    print("Opcion no valida...")      
