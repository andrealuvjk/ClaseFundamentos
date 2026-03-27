#Cree un programa que solicite un nombre completo y lo separe en palabras utilizando el método split().
#Luego muestre cada palabra en una línea diferente.

nombre = input("escriba su nombre completo: ")

nombre = nombre.split()

palabra = nombre

for palabra in nombre: 
    print(palabra)