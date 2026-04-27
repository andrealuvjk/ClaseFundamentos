
num_validos = []  # Lista para almacenar los números válidos ingresados
suma_acumulativa = 0  # Variable para llevar la suma acumulativa

print("La suma acumulativa se detendra automaticamente cuandor resultado sea mayor a 100")
while True:
    num = int(input("\nIngrese un número positivo "))

    if num < 0:
        print("Número inválido. Por favor, ingrese un número positivo.")
   
    elif num > 0:
        suma_acumulativa += num  # Sumar el número a la suma acumulativa
        num_validos.append(num)  # Agregar el número a la lista de válidos
        if suma_acumulativa > 100:
            print(f"Limite alcanzado. La suma acumulativa total {suma_acumulativa} es mayor a 100.")
            break

print("Los números que ayudaron a llegar a la meta fueron:")

for n in num_validos:
    print(n)
    
    
       