class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        

    @staticmethod
    def conectar():
        return sqlite3.connect('escolar.db')

   8