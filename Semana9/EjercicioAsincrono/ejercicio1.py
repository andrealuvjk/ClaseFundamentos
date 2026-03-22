##Cree un programa que solicite al usuario su nombre completo. Luego muestre:
##El nombre en mayúsculas.
## El nombre en minúsculas.
## La cantidad de caracteres que tiene el nombre.

nombre = input("Ingrese un nombre: ")

print("nombre en mayusculas: ")
print(nombre.upper())

print("nombre en minusculas: ")
print(nombre.lower())

print("El nombre tiene las siguientes letras: ")
print(len(nombre.replace(" ", "")))