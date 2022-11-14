import pandas as pd
import matplotlib.pyplot as plt


#Actividad 14
#https://naps.com.mx/blog/ejemplos-en-matplotlib-de-5-tipos-graficos/
#fuente de datos (3) :
    # archivo (txt, csv, )
    # bases de datos (sql: mysql o postgres / entornos nosql: mongodb)
    # webservices, API Rest: petición get: responde xml / json


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def cargar_archivo():

    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Mario-FP\\Programación\Proyectos\\teoria_14112022\\casasboston.csv")
    # datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
    df = datos[["RM", "CRIM", "MEDV", "TOWN", "CHAS"]]  #Selecciona algunas columnas

    df = datos.rename(columns={
        "TOWN": "CIUDAD",
        "CRIM": "INDICE_CRIMEN",
        "INDUS": "PCT_ZONA_INDUSTRIAL",
        "CHAS": "RIO_CHARLES",
        "RM": "N_HABITACIONES_MEDIO",
        "MEDV": "VALOR_MEDIANO",
        "LSTAT": "PCT_CLASE_BAJA"
    })

    #print(df.sample(5))
    #Histograma
    df.N_HABITACIONES_MEDIO.plot.hist()
    plt.show()

    #Gráfico de dispersión
    df.plot.scatter(x="INDICE_CRIMEN", y="VALOR_MEDIANO", alpha=0.2)
    plt.show()

    #Gráfico de barras
    valor_por_ciudad = df.groupby("CIUDAD")["VALOR_MEDIANO"].mean()
    valor_por_ciudad.head(10).plot.barh()
    plt.show()

    #Diagrama de cajas
    df["VALOR_CUANTILES"] = pd.qcut(df.VALOR_MEDIANO, 5)
    df.boxplot(column="INDICE_CRIMEN", by="VALOR_CUANTILES",
               figsize=(8, 6))
    plt.show()

    #Gráfico circular
    df.RIO_CHARLES.value_counts().plot.pie()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    cargar_archivo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
