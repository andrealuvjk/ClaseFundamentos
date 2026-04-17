
#Ejercicio 2:
#Solicita la edad de una persona y muestra si es menor de edad, mayor de edad o adulto mayor (60 o más).



def CalcularEdad(edad):
    if edad >= 60 :
        print("eres un adulto mayor")
    elif edad >= 18:
        print("Eres mayor de edad") 
    elif edad <= 17:
        print("Eres menor de edad") 
    else:
        print("Edad desconocida o ingrese un numero valido(entero)")


edad = int(input("Ingrese su edad: "))

CalcularEdad(edad)
