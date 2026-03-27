#Cree un programa que solicite un correo electrónico y verifique si contiene el símbolo @.
#Si lo contiene, muestre el mensaje: "El correo parece válido".
#Si no lo contiene, muestre el mensaje: "El correo no es válido".

correo = input("Ingrese un correo a verificar como valido: ")

if "@" in correo:
    print("el correo parece valido")
else:
    print("el correo no es valido")