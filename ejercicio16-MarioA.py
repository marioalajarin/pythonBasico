#Ejercicio 2
#La nota del trimestre está basada en
    #Nota hito individual = 30%
    #Nota hito grupal = 20%
    #Nota examen = 50%

#Datos de entrada
    #Nota en el hito individual
    #Nota en el hito grupal
    #Nota en el examen

#Datos de salida
    #Nota total

def notas():

    NHI=float(input("Nota en el hito individual: "))
    NHG=float(input("Nota en el hito grupal: "))
    NE=float(input("Nota en el examen: "))

    NT=(NHI*0.3+NHG*0.2+NE*0.5)
    print(f"La nota es {round(NT)}")
#notas()

#Ejercicio 3
#Se pide calcular la nota de tu examen tipo test.
    #Serán 20 preguntas
    #Las preguntas correctas sumarán 0,5
    #Las preguntas incorrectas restarán 0,25
    #Las preguntas sin contestar tendrán 0

#Datos de entrada
    #Cuantas preguntas son correctas
    #Cuantas preguntas son incorrectas
    #Cuantas preguntas son nulas

#Datos de salida
    #La nota total


def notaNashe():
    ntotal=0
    aciertos=float(input("¿Cuántas has acertado?: "))
    errores=float(input("¿Cuántas preguntas has fallado?: "))
    nulos=float(input("¿Cuántas preguntas no has contestado?: "))

    
    total=ntotal+(aciertos*0.5)-(errores*0.25)+(nulos*0)
    print(f"La nota es {total}")
notaNashe()

#Ejercicio 4
#Diseña un algoritmo y un diagrama de flujo para:
    #Con la base y la altura de un rectángulo, se nos pide calcular su perímetro y su área

#Datos de entrada
    #Cuanto mide de largo
    #Cuanto mide de alto

#Datos de salida
    #El perímetro
    #El área

def rectangulo():
    base=float(input("Ingrese el tamaño de la base del rectángulo: "))
    altura=float(input("Ingrese la altura del rectángulo: "))

    perimetroR=(base*2+altura*2)
    areaR=(base*altura)

    print(f"El perímetro es {perimetroR}m y el area es {areaR}m2.")
#rectangulo()
