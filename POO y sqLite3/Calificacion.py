import sqlite3

class Calificacion:
    def __init__(self, id_estudiante, id_materia, nota, fecha):
        self.id_estudiante = id_estudiante
        self.id_materia = id_materia
        self.nota = nota
        self.fecha = fecha

    @staticmethod
    def conectar():
        return sqlite3.connect('escuela.db')

    def guardar(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO calificacion (id_estudiante, id_materia, nota, fecha)
            VALUES (?, ?, ?, ?)
        ''', (self.id_estudiante, self.id_materia, self.nota, self.fecha))
        conexion.commit()
        conexion.close()
