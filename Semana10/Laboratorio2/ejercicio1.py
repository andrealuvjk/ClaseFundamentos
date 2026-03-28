 #Crear una función que reciba un texto y un número. Según el número:
# 1. Convertir todo el texto a mayúsculas
# 2. Convertir todo el texto a minúsculas
# 3. Colocar la primera letra en mayúscula

def modificar_texto(text, num):
    if num == 1:
        return text.upper() 
    elif num == 2:
         return text.lower()
    elif num == 3:
        return text.capitalize()
    else:
        return "Error. opcion no valida"
    

texto = input("Escriba el texto a modificar: ")
numero =int(input("Escriba un numero (1, 2 o 3): "))

respuesta = modificar_texto(texto,numero)
print("El resultado es: ", respuesta)
