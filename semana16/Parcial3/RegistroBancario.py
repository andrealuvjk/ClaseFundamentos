from decimal import Decimal

print("--- Terminal de Cobro Seguro ---")

# Acumulador en cero
total_acumulado = Decimal('0.00')

while True:
    entrada = input("Ingrese el precio del producto (o '0' para salir): ")
    
    try:
        # Solo lo usamos para forzar el ValueError si hay letras
        detector = float(entrada)
        
      
        if detector == 0.0:
            break
            
        # sumamos usando Decimal
        total_acumulado += Decimal(entrada)
        
    except ValueError:
   
        print("Error, Por favor, ingrese solo números.")


print(f"\nCobro finalizado. El total es: ${total_acumulado}")