#Cree un programa que solicite una frase y cuente cuántas veces aparece la letra "a" dentro de la frase.
#Puede utilizar el método count().

frase = input("Ingrese una frase o palabra: ")

cantidad = frase.count("a")

print(f"la letra 'a' aparece {cantidad} veces")