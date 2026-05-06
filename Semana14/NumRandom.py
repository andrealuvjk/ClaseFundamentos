import random  # Esto SIEMPRE va en la primera línea de tu archivo

# 1. LA MÁQUINA CONTADORA (La función)
def contar_mayores_50(lista_numeros):
    #contador, se guardaran los numeros que son mayores a 50
    mayores = 0
    for numero in lista_numeros:
        if numero > 50:
            mayores += 1  #tambien se puede escribir como: mayores = mayores + 1
    return mayores
            
# lista vacía
numeros_aleatorios = []

for i in range(10):
    numero_generado = random.randint(1, 100)
    numeros_aleatorios.append(numero_generado)
   
print(f"Los 10 números aleatorios generados son: {numeros_aleatorios}")

# Llamar a la funcion
total_encontrados = contar_mayores_50(numeros_aleatorios)

print(f"Se encontraron {total_encontrados} numeros que son mayores a 50.")