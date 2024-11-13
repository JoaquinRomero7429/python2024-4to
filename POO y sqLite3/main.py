from Estudiante import Estudiante


def menu_principal():
    while True:
        print("Sistema Escolar")
        print("1. Agregar Estudiante")
        print("2. Listar Estudiantes")
        print("3. Actualizar Estudiante")
        print("4. Eliminar Estudiante")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            legajo_id = int(input("Ingrese el legajo del estudiante: "))
            dni = int(input("Ingrese el DNI del estudiante: "))
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante (dia/mes/año): ")
            curso = input("Ingrese el curso del estudiante: ")
            estado = input("Ingrese el estado del estudiante: ")
            email = input("Ingrese el email del estudiante: ")
            estudiante = Estudiante(legajo_id, dni, nombre, edad, fecha_nacimiento, curso, estado, email)
            estudiante.guardar()
            print("Estudiante agregado correctamente.")
        
        elif opcion == '2':
            estudiantes = Estudiante.obtener_todos()
            for est in estudiantes:
                print(est)
        
        elif opcion == '3':
            
            pass
        
        elif opcion == '4':
            legajo_id = int(input("Ingrese el legajo del estudiante a eliminar: "))
            estudiante = Estudiante(legajo_id, None, None, None, None, None, None, None)
            estudiante.eliminar()
            print("Estudiante eliminado correctamente.")
        
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
