Algoritmo Lab1
	
	Definir total,num Como Real
	definir contador Como Entero
	
	total = 0
	contador = 0 

	Mientras total <= 75 Hacer   //mientras total de la suma sea menor o igual a 75 se repetira este bucle
		Escribir "Ingrese un numero a sumar" //se le pedira que ingrese un numero
		leer num 
		total = total + num //total se suma con el numero que se ingreso, y se guarda en total
		contador = contador + 1 //cada vez que esto se repita se ira sumando el contador
	
		Si NO (total > 75) Entonces // si total sigue siendo menor a 75 (porque al estar "Si No" se esta negando que total > 75)
			Escribir "Aún no llegamos, llevas: ", total
			
		FinSi
	Fin Mientras
	
	Escribir "Tu resultado es : " total ", mayor a 75!"
	Escribir "Cantidades de numeros ingresados ", contador
	Escribir "Fin del bucle"
	
FinAlgoritmo

