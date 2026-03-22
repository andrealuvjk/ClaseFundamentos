#Solicite al usuario una frase y verifique si la frase termina con un punto ".".
#Puede utilizar el método endswith().

frase = input("Escriba una frase: ")
#El método startswith() es como una pregunta que le haces a la frase: "¿Empiezas con esto?". 
# La respuesta es Sí (True) o No (False).

if frase.endswith("."):
    print("La frase sí termina con '.' (punto)")
else:
    print("La frase no termina con '.'(punto)")
