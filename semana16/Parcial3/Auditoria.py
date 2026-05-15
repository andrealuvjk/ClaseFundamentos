print("--- Auditoría de Registros ---")


for registro in range(1, 51):
    
  
    if registro == 42:
        print(f"Brecha de seguridad en ID: {registro}. Deteniendo sistema.")
        break 
        
    # para múltiplos de 3
    if registro % 3 == 0:
        continue # El continue ignora lo que falta y salta a la siguiente vuelta
        
    print(f"Procesando registro ID: {registro}")

print("--- Auditoría Finalizada ---")