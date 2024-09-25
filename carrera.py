from personaje_clase import Personaje

def pedir_datos_personaje(num):
    
    print(f"Introduce los datos para el personaje {num}:") 
    nombre = input("Nombre: ")
    altura = float(input("Altura: "))
    velocidad = float(input("Velocidad: "))
    resistencia = float(input("Resistencia: "))
    fuerza = float(input("Fuerza: "))
    return Personaje(nombre, altura, velocidad, resistencia, fuerza)

def mostrar_menu():

    print("--- Menú ---")
    print("1. Mostrar información de ambos personajes")
    print("2. Personaje 1 ataca a Personaje 2")
    print("3. Personaje 2 ataca a Personaje 1")
    print("4. Salir")
    return input("Elige una opción: ")

personaje1 = pedir_datos_personaje(1)
personaje2 = pedir_datos_personaje(2)

opcion = ''
while opcion != '4':
    opcion = mostrar_menu()

    if opcion == '1':
        print("Información de los personajes:")
        personaje1.mostrar_info()
        personaje2.mostrar_info()

    elif opcion == '2':
        print("Personaje 1 ataca a Personaje 2:")
        personaje1.atacar(personaje2)

    elif opcion == '3':
        print("Personaje 2 ataca a Personaje 1:")
        personaje2.atacar(personaje1)

    elif opcion == '4':
        print("Saliendo del programa...")

    else:
        print("Opción no válida. Intenta de nuevo.")

