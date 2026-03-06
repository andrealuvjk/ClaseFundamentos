Algoritmo ejercicio2
	Definir suma, num, total Como Entero
	
	total = 0
	
	Repetir
		Escribir "Ingrese numeros positivos a sumar(si es negativo se sale del ciclo)"
		leer num
		si num >= 0 Entonces
			total = total + num
		FinSi
		
	Hasta Que num < 0 
	
	Escribir "El total de la suma de numeros positivos es: ", total
	
FinAlgoritmo
