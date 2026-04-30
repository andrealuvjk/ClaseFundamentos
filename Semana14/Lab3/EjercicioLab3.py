
while True:
    print("\n------Menu principal------")
    print("1. Registrar alumnos y sus calificaciones")
    print("2. Salir del programa")
 
    opcion = int(input("Seleccione una opción: "))

    if opcion == 2:
        print("Saliendo del programa...")
        break
    elif opcion == 1:
        cantidad = int(input("Cuantos alumnos desea registrar? "))

        for i in range(1, cantidad + 1):
            nombre = input("Ingrese el nombre del alumno: ")
            grado = int(input("Ingrese el grado del alumno (1-9): "))
            match grado:
                case 1 | 2 | 3:
                    print(f"El alumno/a {nombre} esta en primer ciclo")
                case 4 | 5 | 6:
                    print(f"El alumno/a {nombre} esta en segundo ciclo")
                case 7 | 8 | 9:
                    print(f"El alumno/a {nombre} esta en tercer ciclo")
                case _:
                    print("Grado no valido, intente de nuevo")
            promedio = float(input("Ingrese el promedio del alumno: "))
            if promedio < 0 or promedio > 10:
                print("Promedio no valido, intente de nuevo")
            elif promedio >= 6:
                print(f"El alumno/a {nombre} esta aprobado")
            else:
                print(f"El alumno/a {nombre} esta reprobado")
    else:
        print("Opcion no valida, intente de nuevo")
         

            