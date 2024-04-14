import pandas as pd

df = pd.read_excel("datos_facturacion.xlsx")
print(df.head())

filtro1=df[(df["CVE_CLPV"] >= 1000) & (df["CVE_CLPV"]<=2000)]
print("Filtro 1")
print(filtro1)
filtro1.to_csv("Practica_facturacion_1.csv")

filtro2 = df[~(df["CVE_VEND"] == 5.0 ) & ~(df["CVE_VEND"] == 4.0)]
print("Filtro 2")
print(filtro2)
filtro2.to_csv("Practica_facturacion_2.csv")


filtro3=df[df["FECHA_ENT"] == '2022-28-2']
print("Filtro 3")
print(filtro3)
filtro3.to_csv("Practica_facturacion_3.csv")


filtro4=df[(df["CAN_TOT"] < 5951.7)| (df["STATUS"] == "E")]
print("Filtro 4")
print(filtro4)
filtro4.to_csv("Practica_facturacion_4.csv")


filtro5 = df.iloc[ : , [0, 6, 7,9]]  
print("Filtro 5")
print(filtro5)
filtro5.to_csv("Practica_facturacion_5.csv")


filtro6 = df.iloc[7001:7099, :  ] 
print("Filtro 6")
print(filtro6)
filtro6.to_csv("Practica_facturacion_6.csv")

df1= pd.read_excel("datos_facturacion.xlsx", index_col=3)
print(df1.head())

filtro7=df1.loc[[1.0,2.0], ["FECHAELAB"]]
print("Filtro 7")
print(filtro7)
filtro7.to_csv("Practica_facturacion_7.csv")




