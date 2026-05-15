import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv

    if len(argv) > 1:
        carpeta_objetivo = Path(argv[1]).expanduser().resolve()
    else:
        carpeta_objetivo = Path.home() / "Downloads"

    if not carpeta_objetivo.is_dir():
        print(f"No existe o no es una carpeta: {carpeta_objetivo}", file=sys.stderr)
        sys.exit(1)

    categorias = {
        "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
        "Documentos": [".pdf", ".docx", ".xlsx", ".txt", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Musica": [".mp3", ".wav"],
    }

    extension_a_categoria: dict[str, str] = {}
    for categoria, exts in categorias.items():
        for ext in exts:
            extension_a_categoria[ext.lower()] = categoria

    archivos = [p for p in carpeta_objetivo.iterdir() if p.is_file()]

    movidos = 0
    for archivo in archivos:
        ext = archivo.suffix.lower()
        categoria = extension_a_categoria.get(ext, "Otros")
        destino_dir = carpeta_objetivo / categoria
        destino_dir.mkdir(exist_ok=True)
        archivo.rename(destino_dir / archivo.name)
        movidos += 1
        print(f"Movido {archivo.name} a {categoria}/")

    resumen = (
        f"Se organizaron {movidos} archivo(s).\n\n"
        f"Carpeta: {carpeta_objetivo}"
        if movidos
        else f"No había archivos sueltos en la carpeta.\n\n{carpeta_objetivo}"
    )
    print("\n--- Tarea terminada ---\n" + resumen + "\n")

    if sys.platform == "win32":
        import ctypes

        ctypes.windll.user32.MessageBoxW(0, resumen, "Organizador de archivos", 0x40)


if __name__ == "__main__":
    main()
