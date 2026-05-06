
def sumar_pares(lista_numeros):
    
    suma_total = 0 
    for numero in lista_numeros:
        
        # Si el residuo de dividir entre 2 es cero, es par
        if numero % 2 == 0:
            # se suma al contador la cantidad del numero actual
            suma_total = suma_total + numero 
    #se retorna la suma total de los numeros pares encontrados en la lista        
    return suma_total




numeros_prueba = [10, 3, 5, 8, 1, 4] 
# La suma de los pares 10 + 8 + 4 debería dar 22
resultado_suma = sumar_pares(numeros_prueba)

# mostrar el resultado
print(f"La lista de números es: {numeros_prueba}")
print(f"La suma total de SOLO los números pares es: {resultado_suma}")