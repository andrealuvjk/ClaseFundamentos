#Ejercicio 4:
#Crear una función que reciba una lista de palabras y un número. 
# La función debe transformar cada palabra de la lista según la opción seleccionada (1, 2 o 3).

def modificar_lista(lista, num):
    resultado = []

    for palabra in lista:
        if num == 1:
            resultado.append(palabra.upper())
        elif num == 2:
            resultado.append(palabra.lower()) 
        elif num == 3:
            resultado.append(palabra.capitalize())
            
            
    return resultado
        
lista_palabras = ["uva", "Melocoton", "SANDIA"]
print(modificar_lista(lista_palabras,1)) 
print(modificar_lista(lista_palabras,2))
print(modificar_lista(lista_palabras,3))  

