#1.- Cargar datos del archivo  csv.
import webbrowser
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv('ventas.csv', sep=";")
#2.- Calcular ventas totales por mes.
df["Fecha"] = pd.to_datetime(df["Fecha"], dayfirst=True)
df["mes"] = df["Fecha"].dt.to_period("M")

ventas_por_mes = df.groupby('mes').apply(lambda d: (d['Cantidad'] * d['Precio']).sum())

ventas_por_mes = ventas_por_mes.sort_index()

print("Ventas por mes:")

print(ventas_por_mes)
#3.- Determinar el producto más vendid y con mayor ingresos.
df['Ingreso'] = df['Cantidad'] * df['Precio']
ventas_prod = df.groupby('Producto').agg({'Cantidad': 'sum', 'Ingreso': 'sum'})
mas_vendido = ventas_prod['Cantidad'].idxmax()
mayor_ingreso = ventas_prod['Ingreso'].idxmax()
print(f"El producto más vendido es: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'Cantidad']})")
print(f"El producto con mayor ingreso es: {mayor_ingreso} (total {ventas_prod.loc[mayor_ingreso, 'Ingreso']:.2}$)")
#4.- Graficar ventas por mes.
import matplotlib.pyplot as plt
ventas_por_mes.index = ventas_por_mes.index.astype(str)
plt.figure(figsize=(6, 4))
ventas_por_mes.plot(kind='bar')
plt.title('Ventas por mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.tight_layout()
plt.savefig('ventas_por_mes.png')
#llamada del archivo html de informe.
informe_html = BASE_DIR / "Informe" / "Informe.html"
if informe_html.is_file():
    webbrowser.open(informe_html.as_uri())
    print(f"Informe abierto en el navegador: {informe_html}")
else:
    print(f"No existe el informe en: {informe_html}")
plt.show()
#5.- Graficar top 5 productos por ingresos.
top5 = ventas_prod.nlargest(5, 'Ingreso')
plt.figure(figsize=(6, 4))
plt.bar(top5.index, top5['Ingreso'])
plt.title('Top 5 productos por ingresos')
plt.xlabel('Producto')
plt.ylabel('Ingresos ($)')	
plt.tight_layout()
plt.savefig('top5_productos_por_ingresos.png')
plt.show()

