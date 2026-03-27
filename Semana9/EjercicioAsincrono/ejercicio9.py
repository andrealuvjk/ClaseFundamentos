#Solicite al usuario una frase y muestre si la frase empieza con la palabra "Hola".
#Puede utilizar el método startswith().

frase = input("Escriba una frase: ")
#El método startswith() es como una pregunta que le haces a la frase: "¿Empiezas con esto?". 
# La respuesta es Sí (True) o No (False).

if frase.startswith("Hola"):
    print("La frase sí empieza con Hola.")
else:
    print("La frase no empieza con Hola.")
