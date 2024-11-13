import sqlite3

class Estudiante:
    def __init__(self, dni, nombre, edad, fecha_nacimiento, curso, estado, email):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
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
            INSERT INTO estudiante (dni, nombre, edad, fecha_nacimiento, curso, estado, email)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self.dni, self.nombre, self.edad, self.fecha_nacimiento, self.curso, self.estado, self.email))
        conexion.commit()
        conexion.close()

    @staticmethod
    def listar():
        conexion = Estudiante.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estudiante")
        estudiantes = cursor.fetchall()
        conexion.close()
        return estudiantes

    @staticmethod
    def actualizar(legajo_id, nombre, edad):
        conexion = Estudiante.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE estudiante 
            SET nombre = ?, edad = ?
            WHERE legajo_id = ?
        ''', (nombre, edad, legajo_id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(legajo_id):
        conexion = Estudiante.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM estudiante WHERE legajo_id = ?", (legajo_id,))
        conexion.commit()
        conexion.close()


   