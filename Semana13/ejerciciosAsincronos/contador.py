
# Contadores iniciales (empiezan en cero porque aún no hemos contado nada)
positivos = 0
negativos = 0


while True: 
    num = int(input("Ingrese un numero o escribir '0' para salir: "))

    if num == 0: 
        print("Saliendo del contador...see ya my friend!")
        break

    if num > 0: 
        positivos += 1
    elif num < 0:
        negativos += 1

    resumen = [f"Total de numeros positivos: {positivos}", f"Total de numeros negativos: {negativos}"]

    print("Resultados de total numeros positivos y negativos:")
    for linea in resumen:
        print(linea)
        