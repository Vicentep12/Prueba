#Perfumes Gloria

print("Bienvenido a perfumes Gloria, a continuación indica tu información:")

nombre = input("Nombre completo: ")
rut = input("N° identificación (RUT): ")

print("A continuacion los 10 productos que estan en el inventario: ")
print("1. Perfume Organza/damas")
print("2. Katy Perry/damas")
print("3. Mañana Fresca/damas")
print("4. La mejor noche/damas")
print("5. Sueño exclusivo/damas")
print("6. Ahora sí voy/caballero")
print("7. Antonio Banderas/caballero")
print("8. Lacoste/caballero")
print("9. Hugo Boss rojo/caballero")
print("10. A que te quito el sueño/caballero")

opcion_perfume = int(input("Selecciona el número del producto que deseas: ")) - 1

print("Precios para los perfumes: ")
print("1.- 100ml $18.000")
print("2.- 50ml $10.000")

tamaño = int(input("¿Qué tamaño deseas? (1 para 100ml, 2 para 50ml): "))

if tamaño == 1:
    print("Has seleccionado la opción de 100ml con un valor de $18.000")
elif tamaño == 2:
    print("Has seleccionado la opción de 50ml con un valor de $10.000")
else:
    print("Opción inválida. Elige 1 para 100ml o 2 para 50ml.")




