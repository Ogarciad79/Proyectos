import tkinter as tk
from tkinter import filedialog, messagebox


def abrir_archivo():
    ruta = filedialog.askopenfilename(
        title="Abrir archivo",
        filetypes=[("Texto", "*.txt"), ("Todos los archivos", "*.*")],
    )
    if not ruta:
        return
    try:
        with open(ruta, encoding="utf-8") as f:
            texto.delete("1.0", tk.END)
            texto.insert("1.0", f.read())
        ventana.title(f"Notas — {ruta}")
    except OSError as e:
        messagebox.showerror("Error al abrir", str(e))


def guardar_archivo():
    ruta = filedialog.asksaveasfilename(
        title="Guardar como",
        defaultextension=".txt",
        filetypes=[("Texto", "*.txt"), ("Todos los archivos", "*.*")],
    )
    if not ruta:
        return
    try:
        contenido = texto.get("1.0", tk.END + "-1c")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        ventana.title(f"Notas — {ruta}")
    except OSError as e:
        messagebox.showerror("Error al guardar", str(e))


def cortar():
    texto.focus_set()
    texto.event_generate("<<Cut>>")


def copiar():
    texto.focus_set()
    texto.event_generate("<<Copy>>")


def pegar():
    texto.focus_set()
    texto.event_generate("<<Paste>>")


ventana = tk.Tk()
ventana.title("Notas")
ventana.geometry("640x480")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir…", command=abrir_archivo)
menu_archivo.add_command(label="Guardar…", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)

menu_edicion = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Edición", menu=menu_edicion)
menu_edicion.add_command(label="Cortar", command=cortar)
menu_edicion.add_command(label="Copiar", command=copiar)
menu_edicion.add_command(label="Pegar", command=pegar)

texto = tk.Text(ventana, wrap=tk.WORD, undo=True)
texto.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

ventana.mainloop()
