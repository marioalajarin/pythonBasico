from bs4 import BeautifulSoup

#muestra por consola los nombres de los productos.
#Puedes utilizar las librerías que hemos comentado en el proyecto adjunto.


with open("almacen2.xml","r") as f:
    data=f.read()
    bs_data = BeautifulSoup(data, "xml")
print(data)



#Para el producto
#producto categoria="monitor" marca="Acer"
#añade un atributo que pone precio = 599,95


for producto in bs_data.find_all("producto",{"categoria":"monitor"},{"marca":"Acer"}):
    producto["precio"]="599.95"
print(bs_data.prettify())




