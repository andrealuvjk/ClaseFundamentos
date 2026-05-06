
def buscar_producto(lista_productos, producto_search):
    encontrado = False # Empieza como falso, porque aún no hemos buscado nada

    # Recorremos la lista para comparar uno por uno
    for producto in lista_productos:
        if producto == producto_search:
               encontrado = True # Si encontramos el producto, cambiamos a verdadero
               break # Ya no necesitamos seguir buscando, así que salimos del ciclo
    if encontrado == True:
                print(f"El producto {producto_search} se encuentra en el inventario.")
    else:
        print(f"El producto {producto_search} no existe en la lista")


productos = []

print("Registro de productos (5 productos)")
 
for producto in range(5):
        nombre_producto = input("Ingrese el nombre del producto: ")
        productos.append(nombre_producto)

print("\n--- Buscador ---")
busqueda = input("Ingrese el nombre del producto que desea buscar: ")


buscar_producto(productos, busqueda)