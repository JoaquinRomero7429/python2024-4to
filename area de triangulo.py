base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
radio = float(input("Ingrese el radio del circulo es: "))

areaRectangulo = base * altura # Calcula el area del triangulo y guarda en la variable
areaCirculo = 3.14 * radio **2 # Calcula el area de la circunferencia y guarda en la variable

def menu():
    multiplicasion = '''
#########################################
#     1 - Calcular Area Triangulo       #
#     2 - Calcular Area Rectangulo      #
#     3 - Salir                         #
######################################### '''

    print(multiplicasion)
    