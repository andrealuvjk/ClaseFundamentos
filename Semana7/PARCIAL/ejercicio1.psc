	Algoritmo ejercicio1
		Definir nota como real 
		
		Escribir "Ingrese nota del estudiante"
		leer nota
		Mientras nota < 0 O nota > 10 Hacer
			Escribir "Error, ingrese una nota entre 0 y 10:"
			leer nota
		Fin Mientras
		
		
		si nota >= 6 Entonces
			escribir "El estudiante aprobo"
		SiNo
			si nota >= 5 Y nota < 6 Entonces
				escribir "el estudiante necesita recuperacion"
			SiNo
				escribir "el estudiante reprobo"
			FinSi
		FinSi
		
	FinAlgoritmo
