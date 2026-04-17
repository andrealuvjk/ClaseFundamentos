
num1 = float(input("ingrese un numero a operar: "))
num2 = float(input("ingrese segundo numero a operar: "))
operacion = input("Seleccione un operador: +,-, * , / ")

if operacion == "+":
    resultado = num1 + num2
    print(f"Resultado de suma es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"Resultado resta: {resultado}")
elif operacion == "*" :
    resultado = num1 * num2
    print(f"Resultado multiplicacion {resultado}")
elif operacion == "/":
    if num2 != 0:
      resultado = num1 / num2
      print(f"Resultado division: {resultado}")
    else:
      print("Error, no se puede dividir entre 0")
else:
    print("Error inesperado")
