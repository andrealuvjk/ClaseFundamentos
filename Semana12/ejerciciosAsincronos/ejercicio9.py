
año = int(input("Ingrese un año para conocer si es bisiesto o no: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
 print("Es un año bisiesto")
else:
 print("No es un año bisiesto")