
while True:

    num = int(input("Ingrese un numero a generar tabla o escribir '-1' para salir: "))

    if num == -1:
        print("Saliendo del programa...Bye bye!")
        break
    
    print(f"Los resultados de la tabla {num} mayor a 20 son: ")

    hubo_mayores_a_20 = False

    for i in range(1,11):

        resultado = num * i

        if resultado > 20:
            print(f"{num} x {i} = {resultado}")
            hubo_mayores_a_20 = True
    if hubo_mayores_a_20 == False:
        print("El numero no cumple con la condicion de ser mayor a 20, se omite el resultado.")
    