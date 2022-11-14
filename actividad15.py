import random
import pandas as pd
import matplotlib.pyplot as plt

num=random.sample(range(1, 100), 10)
num.sort()
print(num)

#--------------------------------------------------------------------

frase=input("Ingresa una frase: ")
letra=input("Elige la cantidad de letras que quieres comprobar: ")

print(f"la frase tiene {frase.count(letra)}.")

#---------------------------------------------------------------------

def archivo_csv():
    datos=pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Mario-FP\\Programación\Proyectos\\teoria_14112022\\casasboston.csv")
    df = datos[["RM", "CRIM", "MEDV", "TOWN", "CHAS"]]

    df = datos.rename(columns={
        "TOWN": "CIUDAD",
        "CRIM": "INDICE_CRIMEN",
        "INDUS": "PCT_ZONA_INDUSTRIAL",
        "CHAS": "RIO_CHARLES",
        "RM": "N_HABITACIONES_MEDIO",
        "MEDV": "VALOR_MEDIANO",
        "LSTAT": "PCT_CLASE_BAJA"
    })

    df.RIO_CHARLES.value_counts().plot.pie()
    plt.show()
archivo_csv()