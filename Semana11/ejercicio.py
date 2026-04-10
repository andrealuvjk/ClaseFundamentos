clima = "caliente" ## clima por defecto

#entrada =input("¿como esta el clima? ")

#print("El clima es: ", entrada)

#f entrada == "frio":
 #print("comprar algodon de azucar")

 #numeroComparar = 21
numeroComparar = False

if numeroComparar == False:
  print("debes de trabajar")
else: 
  print("debes cuidar tus rodillas")

  
# and -> dos true
# or  ->  si tenemos un solo true

numer2 = 50

if numer2 > 24 and numer2 < 30:
  print("El numero es mayor a 24 y menor a 30")
elif numer2 >= 30 and numer2 < 35:
  print("El numero es mayor a 30")
elif numer2 > 35:
  print("El numero es mayor a 35 cliente vip")
else:
  print("El numero es menor a 24")


edad = int(input("Ingrese su edad: "))
edadNumero= int(edad) 

if edadNumero > 18 and edadNumero < 25:
  print("Eres mayor de edad")
elif edadNumero >= 25 and edadNumero < 40:
  print("Eres un adulto joven")
elif edadNumero >= 40 and edadNumero < 80:
  print("Eres un adulto")
elif edadNumero >= 100:
  print("Marciano")
else:
  print("No encontrado")

def cambiarFormato(edad):
  if edad.isdigit():
    return int(edad)
  else:
    print("La edad")

