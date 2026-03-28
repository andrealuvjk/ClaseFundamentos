#Crear una función que reciba un texto y una lista de números (entre 1 y 3). La función debe aplicar cada transformación en orden 
# y devolver el resultado final.

def lista_compuesta(texto,lista_num):

    for num in lista_num:

      if num == 1:
         texto =  texto.upper()
      elif num == 2:
         texto = texto.lower()
      elif num == 3:
         texto = texto.capitalize()
      else:
        return "Opcion invalida"
    return texto
    
texto = "tEXTo de PRUeba"
num = [1, 3]

resultado = lista_compuesta(texto, num)

print("EL RESULTADO FINAL ES:", resultado)
         


