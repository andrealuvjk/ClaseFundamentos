#Solicite al usuario una frase y muestre cuántas letras tiene la frase sin contar los espacios. 
#Puede utilizar el método replace() para eliminar los espacios.

frase = input("Ingrese una frase para conocer sus letras: ")
frase_sin_espacios = frase.replace(" ","")
num_letras = len(frase_sin_espacios)

print("La frase tiene: ")
print(num_letras)

