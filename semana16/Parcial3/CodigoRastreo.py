
codigo = input("Ingrese el código de rastreo: ")

# validacion de seguridad
if codigo == "" or codigo is None:
    print("Error: No se ingreso ningun tipo de codigo.Intente de nuevo")
else:
   #porque el año abarca 4 digitos y el numero de ruta 3 digitos(con el guion)
    categoria = codigo[5:-3] 
    print(f"Categoría del paquete: {categoria}")
    
    ruta = "Ruta Local" if codigo[-2:].upper() == "SV"  else "Ruta Internacional"
    print(f"Tipo de ruta: {ruta}")
    