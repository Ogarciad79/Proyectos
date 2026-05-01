# programa para leer un archivo CSV y calcular estadisticas basicas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Datos.csv", sep=";")

# Intenta convertir columnas de texto a numero (elimina espacios internos)
for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        limpio = df[col].astype(str).str.replace(" ", "", regex=False)
        df[col] = pd.to_numeric(limpio, errors="coerce")

# Selecciona solo columnas numericas para evitar errores con texto
df_numerico = df.select_dtypes(include=["number"])

estadisticas = pd.DataFrame(
    {
        "media": df_numerico.mean(),
        "mediana": df_numerico.median(),
        "desviacion_estandar": df_numerico.std(),
    }
)

print("Estadisticas por columna numerica:\n")
print(estadisticas)

# Grafica de dispersion con las dos primeras columnas numericas
if df_numerico.shape[1] >= 2:
    x_col = df_numerico.columns[0]
    y_col = df_numerico.columns[1]

    plt.figure(figsize=(8, 5))
    plt.scatter(df_numerico[x_col], df_numerico[y_col], color="royalblue")
    plt.title(f"Grafica de dispersion: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("dispersion.png")
    plt.show()
else:
    print("\nNo hay suficientes columnas numericas para la grafica de dispersion.")