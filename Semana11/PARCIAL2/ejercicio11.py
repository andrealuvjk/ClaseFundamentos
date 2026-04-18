
texto = " el nido matinal "
print("texto sin modificar: ", texto)


text_modificado = texto.title().strip()
print(f"texto modificado primera mayuscula y sin espacios: '{text_modificado}'")

text_centrado = text_modificado.center(30, "-")
print("texto centrado: ", text_centrado)