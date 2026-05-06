

def mostrar_nombres_largos(lista_de_nombres):
    print("\n--- Nombres con mas de 5 caracteres ---")
    #ciclo para revisar cada nombre dentro de la lista de nombres
    for nombre in lista_de_nombres:
      if len(nombre) >= 5:
         print(nombre)

# se crea el arreglo vacio, aqui se guardaran los nombres
nombres_ingresados = []

print("Bienvenido. Por favor, ingresa 10 nombres.")
#ciclo para pedir los 10 nombres al usuario
for i in range(10):
   nombre = input("Ingrese un nombre:")
   nombres_ingresados.append(nombre) #con append se agrega el nombre al arreglo

#Se llama a la función
mostrar_nombres_largos(nombres_ingresados)