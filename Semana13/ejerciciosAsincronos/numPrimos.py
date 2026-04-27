
while True:
    num = int(input("Ingrese un numero o escribir '0' para salir: "))

    if num == 0: 
        print("Saliendo del programa...Bye bye!")
        break

    print(f"Los números primos del 1 al {num} son:")

    for i in range(1, num + 1):
        
        # Regla matemática: El número 1 nunca se considera primo, así que lo ignoramos
        if i > 1:
            
            # se asume que i es primo hasta que se compruebe
            es_primo = True
            
            # intenta dividir por i
            # range(2, i) significa que intentará dividir entre 2, 3, 4... hasta un número antes de 'i'
            for j in range(2, i):
                
                # Si 'i' se puede dividir exactamente entre 'j', entonces no es primo
                if i % j == 0:
                    es_primo = False  # falso
                    break             # se rompe el ciclo

            # 3. Al terminar las pruebas, si sobrevivió como True, se imprime
            if es_primo == True:
                print(i)