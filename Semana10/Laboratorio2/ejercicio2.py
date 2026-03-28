#Crear una función que reciba una palabra y un número,
#  y muestre el resultado en pantalla aplicando la transformación correspondiente (1, 2 o 3)

##usare la funcion del ejercicio 1 solo que no devolvere los datos, simplemente los "imprimire"


def mostrar_texto(text, num):
    if num == 1:
        print(text.upper())  
    elif num == 2:
         print(text.lower())
    elif num == 3:
        print(text.capitalize())
    else:
        print("Error. opcion no valida") 
    

mostrar_texto("todo en mayusculas",1)
mostrar_texto("TODO EN MINUSCULA", 2)
mostrar_texto("primera letra mayuscula",3)




