#Ejercicio 1:
#Pide un número al usuario e indica si es positivo, negativo o cero usando if, elif y else.

#float es para convertir el texto a num y comparar
num = float(input("Ingrese un numero: ")) 

if num > 0  :
    print("El numero es positivo")
elif num < 0 : 
    print("El numero es negativo")
else:
    print("el numero es igual a 0 o invalido")
