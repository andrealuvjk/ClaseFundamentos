
dias = ["Lunes", "Martes", "Miercoles","Jueves","Viernes","Sabado","Domingo"]

num = int(input("Ingrese un numero del 1 al 7 para conocer su día: "))

if 1 <= num <= 7:
    print(f"El dia de la semana es: {dias[num - 1]}")
else:
    print("Numero fuera del rango")