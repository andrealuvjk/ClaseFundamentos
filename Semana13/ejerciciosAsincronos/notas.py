notas_validas = []

while True:
    
    nota = float(input("Ingrese una nota (0 a 10) o escriba -1 para terminar: "))

  
    if nota == -1:
        break

    #  'and' para que la nota deba cumplir las dos condiciones
    if nota >= 0 and nota <= 10:
        notas_validas.append(nota)
        print("Nota registrada con éxito.")
    else:
       
        print("Nota inválida. Por favor, ingrese un valor entre 0 y 10.")


if len(notas_validas) > 0:
    suma_total = 0
    
    # El trabajador for recorre nuestra lista de notas limpias
    for n in notas_validas:
        suma_total += n
    
    # El promedio es la suma entre la cantidad de elementos (len)
    promedio = suma_total / len(notas_validas)
    
   
    print(f"Notas válidas ingresadas: {len(notas_validas)}")
    print(f"El promedio final es: {promedio:.2f}") # El :.2f es para mostrar solo 2 decimales
else:
    print("No se ingresaron notas válidas para calcular un promedio.")