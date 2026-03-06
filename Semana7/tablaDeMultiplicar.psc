Algoritmo tablaDeMultiplicar
	
	Escribir "seleccione tabla a crear del 1 al 10"
	leer tabla
	
	definir i Como Entero
	para i <- 0 Hasta  10 Con Paso 1 Hacer
		resultado = tabla * i
		
		Escribir tabla i , " X " , "=", resultado 
	FinPara
	
FinAlgoritmo
