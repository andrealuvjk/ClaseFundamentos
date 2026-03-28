 #Ejercicio 3:
#Solicitar al usuario un texto y un número. Enviar esos datos a una función que aplique la transformación según la opción elegida.

#recicle lo del ejercicio 1, no se si en el 1 queria la muy funcion sola sin pedirle datos al usuario
#pero espero cumpla

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
