
texto = "Ing. Andrea.txt"
print("Texto sin remover: ", texto)

remover_sufijo = texto.removesuffix(".txt").removeprefix("Ing. ")
print("texto sin sufijo 'txt' y sin prefijo 'Ing': ", remover_sufijo)

min = remover_sufijo.lower()
print("texto en minusculas: ", min)

