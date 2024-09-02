class Personaje:
    #atributo de clase
    estado = True #vivo

    def __init__(self,nombre,altura,velocidad,resistencia,fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza 


        