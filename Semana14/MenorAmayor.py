
def ordenar_burbuja(lista):
    n = len(lista) # Guardamos la cantidad de elementos
    
    # controla cuántas pasadas completas se da
    for i in range(n):
        
        #compara de dos en dos
        for j in range(n - 1):
            
            # Si el de la izquierda es mayor que el de la derecha, e4 intercambian sus posiciones
            if lista[j] > lista[j + 1]:
                
                # El truco del intercambio con la variable temporal
                temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal
                
    # se retorna la lista ordenada de menor a mayor
    return lista

numeros_ingresados = []

print("--- Ordenador de Números (De menor a mayor) ---")

# ciclo para pedir 6 números al usuario
for i in range(6):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros_ingresados.append(numero)

print(f"\nLista original (desordenada): {numeros_ingresados}")

# Llamamos a la función y guardamos el resultado
lista_final = ordenar_burbuja(numeros_ingresados)

print(f"Lista final (ordenada): {lista_final}")