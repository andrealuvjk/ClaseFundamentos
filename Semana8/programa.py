texto = input("Ingrese un texto: ")

# Eliminar espacios al inicio y al final
texto_limpio = texto.strip()
print("\nTexto sin espacios al inicio y final:")
print(texto_limpio)

# Mostrar en mayúsculas y minúsculas
print("\nTexto en mayúsculas:")
print(texto_limpio.upper())

print("\nTexto en minúsculas:")
print(texto_limpio.lower())

# Pedir una palabra para analizar
palabra = input("\nIngrese una palabra o letra a buscar: ")

# Contar cuántas veces aparece
cantidad = texto_limpio.count(palabra)
print(f"La palabra/letra '{palabra}' aparece {cantidad} veces.")

# Buscar la posición
posicion = texto_limpio.find(palabra)
if posicion != -1:
    print(f"La primera aparición de '{palabra}' está en la posición {posicion}.")
else:
    print(f"La palabra '{palabra}' no se encontró en el texto.")

# Reemplazar palabra
nueva_palabra = input("\nIngrese una palabra para reemplazarla por otra: ")
reemplazo = input("Ingrese la nueva palabra: ")

texto_reemplazado = texto_limpio.replace(nueva_palabra, reemplazo)
print("\nTexto después del reemplazo:")
print(texto_reemplazado)

# Dividir el texto en lista de palabras
lista_palabras = texto_reemplazado.split()
print("\nLista de palabras:")
print(lista_palabras)

# Unir nuevamente en una cadena
texto_unido = " ".join(lista_palabras)
print("\nTexto unido nuevamente:")
print(texto_unido)