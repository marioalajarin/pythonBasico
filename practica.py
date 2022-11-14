import matplotlib.pyplot as plt
import pandas as pd


#muestra un gráfico
#de uso de m3 y de número de clientes

def cargar():

    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Mario-FP\\Programación\\Proyectos\\teoria_14112022\\Servei_d_aigua_-usos_i_nombre_de_clients-.csv")
    # datos = datos[["Ús","any_","m3_registrats","núm_clients","ObjectId","CODI_ENS","NOM_ENS"]]
    df = datos[["m3_registrats", "núm_clients", "ObjectId", "CODI_ENS", "NOM_ENS"]]  #Selecciona algunas columnas

    df = datos.rename(columns={
        "Ús": "us",
        "any_": "any_",
        "m3_registrats": "m3",
        "núm_clients": "numero_clientes",
        "ObjectId": "ObjectId",
        "CODI_ENS": "CODI_ENS",
        "NOM_ENS": "NOM_ENS"
    })

    # Gráfico de barras
    m3_por_uso = df.groupby("m3")["numero_clientes"].mean()
    m3_por_uso.head(10).plot.barh()
    plt.show()

cargar()