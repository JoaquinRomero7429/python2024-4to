import sqlite3

class Materia:
    def __init__(self, nombre, curso, descripcion, horario, dni_profesor):
        self.nombre = nombre
        self.curso = curso
        self.descripcion = descripcion
        self.horario = horario
        self.dni_profesor = dni_profesor

    @staticmethod
    def conectar():
        return sqlite3.connect('escuela.db')

    def guardar(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO materia (nombre, curso, descripcion, horario, dni_profesor)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.nombre, self.curso, self.descripcion, self.horario, self.dni_profesor))
        conexion.commit()
        conexion.close()


   