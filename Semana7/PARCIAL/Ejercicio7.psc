Algoritmo Ejercicio7
	Definir Num1, Num2, prod,cociente Como Real
	
	Escribir "Ingrese primer numero a multiplicar y dividir"
	leer Num1
	Escribir "Ingrese segundo numero a multiplicar y dividir"
	leer Num2

	Prod = Num1 * Num2
	Escribir "El producto es: ", Prod
	
	si Num2 <> 0 Entonces
		cociente = Num1 / Num2
		Escribir "El cociente es :", cociente
		
	SiNo
		Escribir "Error. No se puede dividir por 0"
	FinSi
	
FinAlgoritmo
