def ingresar_NombreApellido():
    while True:
        nombre = input("Ingrese su nombre y apellido: ")
        if nombre:
            return nombre

def ingresar_RUT():
    while True:
        rut = input("Ingrese su número de identificación (RUT): ")
        if rut:
            return rut

def ingresar_correo():
       while True:
        correo = input("Ingrese su correo electronico: ")
        if correo:
            return correo
    
def seleccionar_carrera():
    carreras = {
        "1":("Ingeneria", ["Desarrollo web", "Desarrollo Movil", "Desarrollo Escritorio"]),
        "2":("Analista",["Analisis de Datos", "Limpieza de Datos", "Creacion de Dashboard"]),
        "3":("Gastronomia",["Historia de la Gastronomía", "Alimentos Naturales", "Sopaipillas"] )
        }

    print("Seleccione una carrera:")
    for clave, valor in carreras.items():
        print(f"{clave}. {valor[0]}")

    opcion = input("Ingrese el número de su carrera: ")

    if opcion in carreras:
        return carreras[opcion]
    else:
        print("Opción inválida, intentelo nuevamente.")
        return seleccionar_carrera()
    
def seleccionar_Especializacion(carrera):
    opciones = carrera[1]

    print("Seleccione una especialización:")
    for i, especialidad in enumerate(opciones, 1):
        print(f"{i}. {especialidad}")

    while True:
        opcion = input("Ingrese el número de su especialización: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(opciones):
            return opciones[int(opcion) - 1]
        print("Opción inválida, inténtelo nuevamente.")


def mostrar_menu():
    print("\nSistema de registro de la Fundación DuocUC")

    estudiante = {
        "Nombre": ingresar_NombreApellido(),
        "RUT": ingresar_RUT(),
        "Correo": ingresar_correo()
    }

    carrera = seleccionar_carrera()
    estudiante["Carrera"] = carrera[0]
    estudiante["Especialización"] = seleccionar_Especializacion(carrera)

    print("\nDatos ingresados:")
    for clave, valor in estudiante.items():
        print(f"{clave}: {valor}")


mostrar_menu()
