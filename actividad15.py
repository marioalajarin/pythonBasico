import random
import pandas as pd
import matplotlib.pyplot as plt

num=random.sample(range(1, 100), 10)
num.sort()
print(num)

#--------------------------------------------------------------------

frase=input("Ingresa una frase: ")
letra=input("Elige la letra que quieres comprobar: ")

print(f"la frase tiene {frase.count(letra)}.")

#---------------------------------------------------------------------

def archivo_csv():
    datos=pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Mario-FP\\Programación\Proyectos\\teoria_14112022\\nuevo.csv")
    df = datos[["QuotaAmount", "StartDate", "OwnerName", "Username"]]

    df = datos.rename(columns={
        "QuotaAmount": "cantidad",
        "StartDate": "fecha",
        "OwnerName": "nombreP",
        "Username": "nombre"
    })

    df.RIO_CHARLES.value_counts().plot.pie()
    plt.show()
archivo_csv()