class profesor:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @staticmethod
    def conectar():
        return sqlite3.connect('escolar.db')

   