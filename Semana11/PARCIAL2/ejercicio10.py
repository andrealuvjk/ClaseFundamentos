
text = "PYthon2026"
print("Texto sin modificar: ", text)

es_numerico = text.isalnum()
print("El texto tiene numeros y letras?", es_numerico)

if es_numerico == True: 
    minusculas = text.lower()
    print("Texto en minusculas: ", minusculas)

    reemplazar = minusculas.replace("2026", "")
    print("Palabra separa de los numeros: ",reemplazar)
else:
    print("El texto no cumple la condicion")