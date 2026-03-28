#Crear una función que reciba un texto y un número, transforme el texto según la opción y luego devuelva la cantidad de caracteres del resultado

def contar_texto(texto,num):
    if num == 1: 
     texto_mod = texto.upper()
     print("en mayusculas: ", texto_mod)
     return len(texto_mod)
    elif num == 2:
        texto_mod = texto.lower()
        print("en minisculas", texto_mod)
        return len(texto_mod)
    elif num == 3:
        texto_mod = texto.capitalize()
        print("primera letra mayuscula", texto_mod)
        return len(texto_mod)
    else:
     return "Opcion invalida"

    
texto = input("Escriba el texto a modificar: ")
numero =int(input("Escriba un numero (1, 2 o 3): "))

respuesta = contar_texto(texto,numero)
print(respuesta)