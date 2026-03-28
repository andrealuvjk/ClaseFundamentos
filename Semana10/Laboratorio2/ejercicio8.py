#Crear un programa con menú que permita al usuario ingresar un texto y elegir una opción (1, 2 o 3).
#  El programa debe usar una función para aplicar la transformación seleccionada.

def modificar_texto(texto, num):
    if num == 1:
        return texto.upper() 
    elif num == 2:
         return texto.lower()
    elif num == 3:
        return texto.capitalize()
    else:
        return "Error. opcion no valida"
    
while True:
    
    print("\n-----Programa: Transformacion de texto-----")
    print("---Seleccione una opcion para convertir el texto---")
    print("1. convertir a mayusculas") 
    print("2. convertir a minusculas")
    print("3. convertir primera letra mayuscula")
    print("4. Salir del programa")

    opcion = int(input("elige una opcion(1, 2, 3 o 4): "))

    if opcion == 4:
         print("Saliendo del programa...")
         break 
    elif opcion == 1 or opcion == 2 or opcion == 3:

        texto = input("Escribe el texto a modificar: ") 
        resultado = modificar_texto(texto, opcion)

        print("El resultado es: ", resultado)
    else:
        print("Error.Digite una opción del 1 al 4")