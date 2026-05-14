import os
from pathlib import Path
carpeta_objetivo = Path.home() /"Downloads"
categorias = {
    "Imagenes" :[ ".png", ".jpg", ".jpeg", ".gif"],
    "Documentos":[".pdf", ".docx", ".xlsx", ".txt",".pptx"],
    "Videos":[".mp4", ".avi", ".mkv"],
    "Musica":[".mp3", ".wav"], 
}
categorias_predeterminadas = ["Otros"] #entraran lo que no encaje en las anteriores

extension_a_categoria = {}
for categoria, exts in categorias.items():
    for ext in exts:
        extension_a_categoria[ext.lower()] = categoria

archivos = [p for p in carpeta_objetivo.iterdir() if p.is_file()]

for archivo in archivos:

    ext = archivo.suffix.lower()

    categoria = extension_a_categoria.get(ext, "Otros")

    destino_dir = carpeta_objetivo / categoria

    destino_dir.mkdir(exist_ok=True)

    archivo.rename(destino_dir / archivo.name)

    print(f"Movido {archivo.name} a {categoria}/")