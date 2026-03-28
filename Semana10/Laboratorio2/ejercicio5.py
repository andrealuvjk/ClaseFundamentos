#Crear una función que reciba un texto y un número. Si el número no es 1, 2 o 3, debe mostrar un mensaje de “opción inválida”.


def modificar_texto(text, num):
    if num == 1:
        return text.upper() 
    elif num == 2:
         return text.lower()
    elif num == 3:
        return text.capitalize()
    else:
        return "opcion invalida"
    

texto = input("Escriba el texto a modificar: ")
numero =int(input("Escriba un numero (1, 2 o 3): "))

respuesta = modificar_texto(texto,numero)
print("El resultado es: ", respuesta)