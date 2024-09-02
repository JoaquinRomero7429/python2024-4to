from Personaje_clase import Personaje 

p1 = Personaje("Leo" , 100,80,90,70)
print(f"el personaje se llama {p1.nombre}")
def crear_personaje():
    nombre = input("Ingrese el nombre del personaje: ")
    altura = float(input("Ingrese la altura del personaje: "))
    velocidad = float(input("Ingrese la velocidad del personaje: "))
    resistencia = float(input("Ingrese la resistencia del personaje: "))
    fuerza = float(input("Ingrese la fuerza del personaje: "))

    return Personaje(nombre, altura, velocidad, resistencia, fuerza)