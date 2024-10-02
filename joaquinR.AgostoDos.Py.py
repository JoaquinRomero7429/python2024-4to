tareas = []

while True:
    print("****************************")
    print("        MENÚ DE OPCIONES     ")
    print("****************************")
    print("1: Añadir tarea")
    print("2: Ver tareas")
    print("3: Completar tarea")
    print("4: Salir")
    print("****************************")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Descripción de la tarea: ")
        tareas.append(tarea)

    elif opcion == "2":
        if tareas:
            for i in range(1, 999):
                if i <= len(tareas):  
                    print(f"{i}. {tareas[i - 1]}")
                else:
                    break
        else:
            print("No hay tareas.")

    elif opcion == "3":
        if tareas:
            num = int(input("Número de tarea completada: ")) - 1
            if num >= 0 and num < 999:  
                if num < len(tareas):  
                    tareas.pop(num)  
                else:
                    print("Número inválido.")
            else:
                print("Número inválido.")
        else:
            print("No hay tareas para completar.")

    elif opcion == "4":
        print("Gracias por utilizar este programa")
        break
