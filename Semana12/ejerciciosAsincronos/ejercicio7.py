
monto = float(input("Ingrese el monto de su compra: "))

if monto > 100:
    descuento = monto * 0.2
    total = monto - descuento
    print(f"El monto con 20% descuento es: {total}")
elif 50 <= monto <= 100:
    descuento = monto * 0.1
    total = monto - descuento
    print(f"El monto con 10% descuento es: {total}")
elif monto < 50:
    print(f"No tienes descuentos, total es: {monto}")
else:
    print("Error inesperado")