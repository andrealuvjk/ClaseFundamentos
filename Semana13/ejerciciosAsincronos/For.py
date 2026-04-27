


 
while True:
   
    num = int(input("Ingrese un numero o escribir '0' para salir: "))

   
    if num == 0: 
      
        print("Saliendo del programa...Bye bye!")
        break

    print(f"Los numeros pares de {num} son: ")

   
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
