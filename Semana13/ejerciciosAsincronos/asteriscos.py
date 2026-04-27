while True:
    num = int(input("\nIngresa el tamaño del triángulo (o 0 para salir): "))

   
    if num == 0:
        print("Saliendo del programa... Dibujos terminados!")
        break

    print(f"\nAquí tienes tu triángulo de tamaño {num} (solo filas impares):")

    for i in range(1, num + 1):
        if i % 2 == 1:
            print("*" * i)