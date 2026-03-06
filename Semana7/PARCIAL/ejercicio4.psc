Algoritmo ejercicio4
	Definir Num, i Como Entero
	
	Escribir "Ingrese un numero a mostrar sus pares"
	leer Num 
	
	Mientras Num <= 0 Hacer
		Escribir "numero debe de ser positivo y diferente de 0, repita"
		leer Num
	FinMientras
	
	Escribir "los primeros numeros para " , Num " pares son:"
	
	Para i <- 1 Hasta Num * 2 Hacer
		Si i MOD 2 = 0 Entonces
			Escribir i
		FinSi
	Fin Para
	
	
	
	
FinAlgoritmo
