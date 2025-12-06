estudiantes = []

while True:
    print("\n1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Mostrar estudiante con mejor promedio")
    print("4. Buscar por nombre")
    print("5. Eliminar por nombre")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        promedio = float(input("Ingrese promedio: "))
        
        nuevo_estudiante = {
            "nombre": nombre,
            "edad": edad,
            "promedio": promedio
        }
        estudiantes.append(nuevo_estudiante)
        print("\n--------------Estudiante agregado----------------")

    elif opcion == "2":
        for est in estudiantes:
            print(est)

    elif opcion == "3":
        if len(estudiantes) > 0:
            mejor = estudiantes[0]
            for est in estudiantes:
                if est["promedio"] > mejor["promedio"]:
                    mejor = est
            print(f"\nMejor estudiante{mejor}")
        else:
            print("\n No hay estudiantes registrados")

    elif opcion == "4":
        busqueda = input("Ingrese nombre a buscar: ")
        encontrado = False
        for est in estudiantes:
            if est["nombre"] == busqueda:
                print(f"\n{est}")
                encontrado = True
        if not encontrado:
            print("<\n No se encontró al estudiante")

    elif opcion == "5":
        eliminar = input("Ingrese nombre a eliminar: ")
        indice = -1
        for i in range(len(estudiantes)):
            if estudiantes[i]["nombre"] == eliminar:
                indice = i
                break
        
        if indice != -1:
            estudiantes.pop(indice)
            print("\n------Estudiante eliminado----------")
        else:
            print("\nNo se encontró al estudiante")

    elif opcion == "6":
        break

    else:
        print("Opción no válida")