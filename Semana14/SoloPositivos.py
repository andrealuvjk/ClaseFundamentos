
def obtener_positivos(lista_original):
    
    lista_positivos = []
    
    for numero in lista_original:
        if numero > 0:
            lista_positivos.append(numero)
    return lista_positivos

numeros = [-5, 10, -3, 8, 0, 21, -1]

# se llama la funcion para obtener solo los positivos de la lista original
resultado_positivos = obtener_positivos(numeros)

print("La lista original era:", numeros)
print("La lista solo con positivos es:", resultado_positivos)