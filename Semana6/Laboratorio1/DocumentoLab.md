# Laboratorio 1, Fundamentos de Programación

## Algoritmo a resolver en Pseint: Sumar hasta que total sea mayor que 75 usando Hacer-Mientras. 
**Estudiante:** Ochoa Amaya Fátima Andrea

Primero declaramos las variables: 

```vbnet
Definir total, num Como Real
	definir contador Como Entero
```
- total almacenara el valor de la suma y funcionara para comparar cuando el valor es mayor a 75 para parar el bucle.
- num almacenara lo que el usuario ingresara
- contador nos dara el dato para conocer cuantos números se han ingresado o las veces que se repitio antes de dar el resultado.


Luego se inicializan las variables: 
```vbnet  
 total = 0
contador = 0 
 ```

Y se hace uso de la estructura Mientras:

```vbnet 
Mientras total <= 75 Hacer  //mientras total de la suma sea menor o igual a 75 se repetira este bucle
		Escribir "Ingrese un numero a sumar"   //se le pedira que ingrese un numero
		leer num   //se lee
		total = total + num    //total se suma con el numero que se ingreso, y se guarda en total
		contador = contador + 1    //cada vez que esto se repita se ira sumando el contador
```
Después dentro del bucle: 
```vbnet
	Si NO (total > 75) Entonces     // si total sigue siendo menor a 75 (porque al estar "Si No" se esta negando que total > 75)
			Escribir "Aún no llegamos, llevas: ", total  

		FinSi
Fin Mientras
```

Finalmente se rompe el bucle
```vbnet 
Escribir "Tu resultado es : " total ", mayor a 75!"
	Escribir "Cantidades de numeros ingresados ", contador
	Escribir "Fin del bucle"
```
Ahora viendo el bucle en ejecución

```text 
*** Ejecución Iniciada. ***
Ingrese un numero a sumar
> 45
Aún no llegamos, llevas: 45
Ingrese un numero a sumar
> 20
Aún no llegamos, llevas: 65
Ingrese un numero a sumar
> 10
Aún no llegamos, llevas: 75
Ingrese un numero a sumar
> 10
Tu resultado es : 85, mayor a 75!
Cantidades de numeros ingresados 4
Fin del bucle
*** Ejecución Finalizada. ***
```
Como se puedo evidenciar, mientras el resultado de total no se a mayor a 75 el ciclo no se rompe, sigue pidiendole al usuario que ingrese nuevamente el número, y asi sucesivamente hasta romper el bucle. 

Aqui el algoritmo completo de Pseint: 

```vbnet
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

```

