#programa para contar palabras en un archivo de texto.
#pedir al usuario que ingrese el nombre del archivo de texto.
archivo = input("Introduce el nombre del archivo de texto: ").strip()

try:
    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print(f"El archivo {archivo} no existe.")
    raise SystemExit(1)

#separar las palabras.
import re

palabras = re.findall(r"\w+", texto.lower())
total_palabras = len(palabras)
print(f"Total palabras: {total_palabras}")

#Mostrar las 10 palabras más repetidas.
from collections import Counter

contador = Counter(palabras)
mas_comunes = contador.most_common(10)
print("Palabras más comunes:")
for palabra, frecuencia in mas_comunes:
    print(f"{palabra}: {frecuencia}")