import sqlite3

class Profesor:
    def __init__(self, dni_id, nombre, apellido, curso, estado, email):
        self.dni_id = dni_id
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.estado = estado
        self.email = email

    @staticmethod
    def conectar():
        return sqlite3.connect('escuela.db')

    def guardar(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO profesor (dni_id, nombre, apellido, curso, estado, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.dni_id, self.nombre, self.apellido, self.curso, self.estado, self.email))
        conexion.commit()
        conexion.close()

    @staticmethod
    def listar():
        conexion = Profesor.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM profesor")
        profesores = cursor.fetchall()
        conexion.close()
        return profesores


   