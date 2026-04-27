import random #es una libreria para generar numeros aleatorios


# se elige un numero secreto entre 1 y 20 usando la funcion randint de la libreria random
numero_secreto = random.randint(1, 20)
intentos_realizados = []

print("Vamos a jugar a 'Adivina el Número Secreto'!")
print("He pensado un número entre 1 y 20. ¿Puedes adivinarlo? Intentalo!")

while True:
    intento = int(input("\nIngresa tu número: "))
    
    # se guarda el numero del usuario en la lista de intentos
    intentos_realizados.append(intento)

    # Usamos if para dar pistas o terminar el juego
    if intento == numero_secreto:
        print(f"Lo lograste!! El número era {numero_secreto}.")
        break # se rompe el ciclo porque el juego terminó
    elif intento < numero_secreto:
        print("Pista: El número secreto es MAYOR.")
    else:
        print("Pista: El número secreto es MENOR.")


print("Historial de intentos:")
print(f"Te tomó {len(intentos_realizados)} intentos ganar.") #len cuenta la cantidad para mostrar

# con for se recorre la lista de intentos para mostrar su historial
for i in intentos_realizados:
    if i == numero_secreto:
        print(f"Intentaste con {i} -> Bingo!")
    else:
        print(f"Intentaste con {i} -> Fallido")