

nota = float(input("Ingrese una nota: "))

#al usar 0 <= nota <= 5: es para especificar un rango es como decir nota >= 0 && nota <= 5 
#match es el switch case 
#se puede usar match variable o match true, el true es cuando se va a evaluar condiciones logicas
# el _ significa "calquier valor" y por eso se junta con el if porque esa es la condicion que cualquier valor debe de hacer
match nota:
    case 9 | 10:
     print("Excelente")
    case 7 | 8:
      print("Bueno")
    case 6:
     print("Aprobado")
    case _ if 0 <= nota <= 5: 
     print("Reprobado")
    case _:
     print("Nota invalida")

      