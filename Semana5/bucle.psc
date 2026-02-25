Algoritmo bucle
	//contador i i++ i-- contador =+ contador + contador
	//es algo que se repite hasta que una condicion logica la rompe
	Definir contador Como Entero
	Escribir "Numero del 0 al 100"
	leer numeroEntrada
	contador = 0 
	resultado = 0
	suma = 0
	anterior = 0
	
	mientras contador <= numeroEntrada 
		anterior = resultado
		contador = contador + 1 
		resultado = contador + anterior
		
		Escribir "Resultado es ", contador , " + ", anterior, " = ", resultado
	FinMientras
	
	Escribir  " escriba password "
	leer pass
	
	Mientras pass <> "nombre de ella + fecha especial"   // ! = <> < >
		Escribir  "romper bucle infinito 1 si 2 no "
		leer respuesta
		si respuesta == "no"
		FinSi
		si respuesta == "si"
			pass = "nombre de ella + fecha especial"
		FinSi
	FinMientras
	
	Escribir  "final" 
	
FinAlgoritmo
