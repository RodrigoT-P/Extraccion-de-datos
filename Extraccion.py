import pandas as pd

print("Aplicación de extracción de datos")
df = pd.read_excel("detalle_precios_productos_fabricados_2022.xlsx")
#print(df.info)

#print(df.head())

#FILTRO 1 - FILTRO POR OBJETO
filtro1 = df[df["NOMBRE_VENDEDOR"] == "LETICIA RAMIREZ HERNANDEZ"]
#print(filtro1)
filtro1.to_csv("Entregable1.csv")

#FILTRO 2 - FILTRO POR NUMERO DE FILA
filtro2 = df.iloc[2:8,:]
#print(filtro2)
filtro2.to_csv("Entregable2.csv")

#FILTRO 3 - FILTRO POR COLUMNAS
filtro3 = df.iloc[2:5 , [1, 3, 4, 10]]
#print(filtro3)
filtro3.to_csv("Entregable3.csv")

#FILTRO4 - FILTRO DE FILAS CON COLUMNAS
df1 = pd.read_excel("detalle_precios_productos_fabricados_2022.xlsx", index_col=1)
filtro4 = df1.loc[["2022-11-22", "2022-12-23"], ["SUBTOTAL_PARTIDA"]]
#print(filtro4)
filtro4.to_csv("Entregable4.csv")

#FILTRO5 - df.head
filtro5 = df.head(8)
#print(filtro5)
filtro5.to_csv("Entregable5.csv")

#FILTRO 6 - COMPARACIÓN PARA OBTENER DATOS
filtro6 = df[df["SUBTOTAL_PARTIDA"] > 77000]
#print(filtro6)
filtro6.to_csv("Entregable6.csv")

#FILTRO 7 - CONDICIONES
filtro7 = df[(df["SUBTOTAL_PARTIDA"] > 77000) & (df["FECHA_DOC"] == "2022-05-24")]
#print(filtro7)
filtro7.to_csv("Entregable7.csv")

#FILTRO 8
filtro8 = df[(df["SUBTOTAL_PARTIDA"] > 77000)| (df["FECHA_DOC"] == "2022-05-24")]
#print(filtro8)
filtro8.to_csv("Entregable8.csv")

#FILTRO9 
filtro9 = df[~(df["SUBTOTAL_PARTIDA"] > 77000) & ~(df["FECHA_DOC"] == "2022-05-24")]
print(filtro9)
filtro9.to_csv("Entregable9.csv")
