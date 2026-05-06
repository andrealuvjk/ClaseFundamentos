

def Num_Mayor(lista_numeros):
        numero = max(lista_numeros)
        print(f"El número mayor es: {numero}")
        

num_ingresados = []


for i in range(8):
    numero = int(input("Ingrese un número entero a comparar: "))
    num_ingresados.append(numero)
    

Num_Mayor(num_ingresados)