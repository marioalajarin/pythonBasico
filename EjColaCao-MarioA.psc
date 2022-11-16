Algoritmo EjColaCao

	Escribir "¿El ColaCao está hecho?"
	Leer hecho
	
	Si hecho=="si" Entonces
		Escribir "Me sirvo el ColaCao que ya está hecho"
	SiNo
		Escribir "No hay, me voy a hacer uno"
		Escribir "¿Hay leche?"
		leer leche
		Si leche=="si" Entonces
			Escribir "¿Hay cacao en polvo?"
			Leer cacao
			Si cacao=="si" Entonces
				Escribir "Echalo en la leche y ya tienes el ColaCao listo"
			SiNo
				Escribir "Hay que comprar cacao y leche"
			Fin Si
		SiNo
			Escribir "Hay que comprar leche"
		Fin Si
	Fin Si
	
FinAlgoritmo
