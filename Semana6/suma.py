# para declarar una variable en python 
nombre = "Andrea"
print(nombre)
# nombre = 40
edad = 19
#print(nombre)
print(nombre, edad, "anios") #se llama concatenar, no se pueden sumar pq son de diferentes tipos

# las variables pueden ser inmutables,
#  pero siempre deben de conservar su tipo
#las variables tienen tipo => numerico o string (booleano), decimal, entero, float etc.

##para los textos largos vamos a utilizar las comillas triples
texto_largo = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore
 magna aliqua.
 Sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua"""
print(texto_largo)
##estas comillas permiten que el texto se muestre tal cual se a escrito dentro
#de ellas

numero1 = 10
numero2 = 20
resultado = numero1 + numero2
print("el resultado de la suma es ", resultado)

resultado = numero1 - numero2
print("el resultado de la resta es ", resultado)

resultado = numero1 / numero2
print("el resultado de la division es ", resultado)

resultado = numero1 * numero2
print("el resultado de la multiplicacion es ", resultado)