
def contar_pares_impares(lista): 
    pares = 0
    impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros = [4, 7, 2, 9, 10, 15, 8]

total_pares, total_impares = contar_pares_impares(numeros)

print(f"Hay {total_pares} números pares.")
print(f"Hay {total_impares} números impares.")