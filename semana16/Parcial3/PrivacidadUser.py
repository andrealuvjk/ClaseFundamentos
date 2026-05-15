print("--- Sistema de Privacidad de Nombres ---")

nombre_completo = input("Ingrese su nombre y apellido: ")

lista_nombre = nombre_completo.split() # Esto convierte el string en una lista de palabras

lista_invertida = lista_nombre[::-1] # Esto le da la vuelta a la lista usando slicing

print("\n--- Nombre Formateado ---")

# Recorre las palabras de lista invertida
for palabra in lista_invertida:
    palabra_formateada = "" # Acumulador de letras y puntos
    for letra in palabra:
        palabra_formateada += letra + "."
    
    print(palabra_formateada[:-1])