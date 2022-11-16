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
    print(f"La nota es {NT}")
notas()

#Ejercicio 3
#Se pide calcular la nota de tu examen tipo test.
    #Serán 20 preguntas
    #Las preguntas correctas sumarán 0,5
    #Las preguntas incorrectas restarán 0,25
    #Las preguntas sin contestar tendrán 0

#Datos de entrada
    #Respuesta de la pregunta

#Datos de salida
    #La nota total

notaT=0
def notaNashe():
    for pregunta in range(20):
        respuesta=input("Ingrese si su respuesta es correcta: ")
        if respuesta.lower()=="si":
            notaT=notaT+0.5
        if respuesta.lower()=="no":
            notaT=notaT-0.25
        if respuesta.lower()=="":
            notaT=notaT
        print(notaT)
notaNashe()

#Ejercicio 4
#Diseña un algoritmo y un diagrama de flujo para:
    #Con la base y la altura de un rectángulo, se nos pide calcular su perímetro y
    #su área

def rectangulo():
    base=float(input("Ingrese el tamaño de la base del rectángulo: "))
    altura=float(input("Ingrese la altura del rectángulo: "))

    perimetroR=(base*2+altura*2)
    areaR=(base*altura)

    print(f"El perímetro es {perimetroR}m y el area es {areaR}m2.")
rectangulo()
