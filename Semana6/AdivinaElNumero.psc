Algoritmo AdivinaElNumero
	// un inicio y final para que no sea infinito
	// pedir un numero y definir otro para comparar
	Definir intento, seleccion Como Entero
	seleccion = 10
	Escribir 'dime un numero de 0 a ', 10
	Leer intento
	
	// tiene que hacerse algo que sea verdadero falso
	// == para comparar, <> diferente
	
	Mientras seleccion <> intento Hacer
		Escribir 'dime un numero de 0 a ', 10
		Leer intento
	Fin Mientras
	Escribir "Felicidades, pasaste"
	
FinAlgoritmo
