pwd = "andrea2006"
contador = 0
lista_fallos = []

while True:

    user_pwd = input("Ingrese su contraseña (o escriba 0 para salir): ")

    if user_pwd == "0":
        print("Saliendo de la autenticacion...!")
        break

    if user_pwd == pwd:
        print("Contraseña correcta, bienvenido!")
        break
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")
        contador += 1  # Sumamos 1 al contador
        lista_fallos.append(user_pwd)  # Guardamos el intento fallido en la lista


print(f"Hubo un total de {contador} intentos fallidos.")
