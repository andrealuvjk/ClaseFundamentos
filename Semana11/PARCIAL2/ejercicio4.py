
texto = "CANTANDO"

minusculas = texto.lower()
print("Texto en minusculas: ", minusculas)

remover = minusculas.removesuffix("ando")
print("palabra sin el sufijo: ", remover)

encontrar = remover.find("t")
print("la letra t se encuentra en el indice: ", encontrar)