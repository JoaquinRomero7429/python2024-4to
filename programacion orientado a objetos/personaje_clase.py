class Personaje:
    estado = True
    vida = 100
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza, ):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = Personaje.estado 
        self.vida = Personaje.vida  

    def atacar(self, otro_personaje):

        if not self.estado:
            print(f"{self.nombre} está muerto y no puede atacar.")
            return
        if not otro_personaje.estado:
            print(f"{otro_personaje.nombre} ya está muerto, no puede ser atacado.")
            return

        dano = self.fuerza - otro_personaje.resistencia
        if dano < 0:
            dano = 0  

        print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {dano} de daño.")
        otro_personaje.recibir_dano(dano)
        print(f"{otro_personaje.nombre} le quedan {otro_personaje.vida} puntos de vida.")

    def recibir_dano(self, cantidad):
        self.vida -= cantidad  
        if self.vida <= 0:
            self.vida = 0
            self.estado = False
            print(f"{self.nombre} ha muerto.")
        else:
            print(f"{self.nombre} ha recibido {cantidad} de daño. Vida restante: {self.vida}")

    def mostrar_info(self):
        estado_texto = "Vivo" if self.estado else "Muerto"
        print(f"Nombre: {self.nombre}, Altura: {self.altura}, Velocidad: {self.velocidad}, "
              f"Resistencia: {self.resistencia}, Fuerza: {self.fuerza}, Estado: {estado_texto}, Vida: {self.vida}")





