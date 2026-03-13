Algoritmo ejercicio9
	Definir esDivisible Como Logico
	Definir num como Real 
	
	Escribir "Ingrese un numero entero"
	leer num
	
	Mientras num <> TRUNC(num) Hacer  //trunc para conocer si el num tiene decimales.
		Escribir "Error: El numero no puede tener decimales, intente otra vez"
		Leer num
	Fin Mientras
	
	Si num MOD 3 = 0 O num MOD 5 = 0 Entonces 
		esDivisible = Verdadero
	SiNo
		esDivisible = Falso
	FinSi
	Escribir "¿El numero ", num, " se puede dividir? ", esDivisible 
	
FinAlgoritmo
