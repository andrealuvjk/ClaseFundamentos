Algoritmo Lab1
	
	Definir total,num Como Real
	definir contador Como Entero
	
	total = 0
	contador = 0 

	Mientras total <= 75 Hacer
		Escribir "Ingrese un numero a sumar"
		leer num 
		total = total + num
		contador = contador + 1
	
		Si NO (total > 75) Entonces
			Escribir "Aún no llegamos, llevas: ", total
			
		FinSi
	Fin Mientras
	
	Escribir "Tu resultado es : " total ", mayor a 75!"
	Escribir "Cantidades de numeros ingresados ", contador
	Escribir "Fin del bucle"
	
FinAlgoritmo

