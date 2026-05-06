def mayores_edad(lista_edades):
    mayores = []
    
    for edad in lista_edades:
        if edad >= 18:
            mayores.append(edad)
    return mayores

edades = [15, 22, 17, 30, 12, 18, 25]

resultado_mayores = mayores_edad(edades)

print("Las edades originales eran:", edades)
print("Las edades mayores o iguales a 18 son:", resultado_mayores)