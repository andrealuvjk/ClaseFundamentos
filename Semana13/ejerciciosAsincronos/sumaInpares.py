
suma = 0
numeros_impares = [] 


while True:
    num = int(input("\nIngrese un numero o escribir '0' para mostrar el resultado: "))

    if num == 0: 
        print("Saliendo de la captura de datos...\n")
        break

    
    if num % 2 == 1:
        suma += num                  
        numeros_impares.append(num)  


print("--- RESUMEN ---")
print(f"La suma total de los impares es: {suma}")
print("Los números impares que ingresaste fueron:")


for i in numeros_impares:
    print(i)