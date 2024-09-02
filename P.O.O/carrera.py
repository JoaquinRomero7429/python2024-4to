from Personaje_clase import Personaje

def crear_personaje():
    nombre = input("Ingrese el nombre del personaje: ")
    altura = float(input("Ingrese la altura del personaje: "))
    velocidad = float(input("Ingrese la velocidad del personaje: "))
    resistencia = float(input("Ingrese la resistencia del personaje: "))
    fuerza = float(input("Ingrese la fuerza del personaje: "))

    return Personaje(nombre, altura, velocidad, resistencia, fuerza)

def mostrar_personajes(personajes):
    if personajes == []:  
        print("No hay personajes creados.")
    else:
        contador = 1
        for personaje in personajes:
            print(f"Personaje {contador}:")
            print(personaje)
            contador += 1

def menu():
    personajes = []
    
    while True:
        print("Menú:")
        print("1. Crear Personaje")
        print("2. Mostrar Personajes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            personaje = crear_personaje()
            personajes.append(personaje)
            print("El personaje fue creado.")
        elif opcion == '2':
            mostrar_personajes(personajes)
        elif opcion == '3':
            print("gracias por utilizar este programa.")
            break
        else:
            print("Opción invalida, por favor intente de nuevo.")

menu()

