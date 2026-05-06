

def calcular_promedio(lista_notas):
    suma_total = sum(lista_notas) #con sum se suma todos los elementos dentro de un arreglo
    cantidad_notas = len(lista_notas) #para contar cuantos elementos hay dentro de la lista y asi dividir entre la suma
    promedio = suma_total / cantidad_notas
    return promedio
    
# Arreglo de notas de los alumnos
notasAlumnos = [ 5.5,3.0,4.0,7.0,6.0] 

promedioGrupo = calcular_promedio(notasAlumnos)

if promedioGrupo >= 6.0:
    print("¡El grupo APRUEBA!")
else:
    print("El grupo REPRUEBA.")

print(f"El promedio general del grupo es: {promedioGrupo}")