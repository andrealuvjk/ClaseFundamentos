print("--- Sensores Industriales ---")


lecturas = []

for i in range(5):
    # Aseguramos que la entrada se convierta a número entero (int)
    temp = int(input(f"Ingrese la lectura de temperatura {i + 1}: "))
    lecturas.append(temp)

print("\n--- Resultados de Alertas ---")


for temp in lecturas:
    match temp:
        case 0:
            print(f"[{temp}°] Alerta: Punto de Congelación")
            
        case 100:
            print(f"[{temp}°] Alerta: Punto de Ebullición")
            
        case _:
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(f"[{temp}°] {estado}")