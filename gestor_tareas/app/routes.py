from flask import Blueprint, redirect, render_template, request, url_for

from .task_store import agregar_tarea, completar_tarea, listar_tareas

bp = Blueprint("main", __name__)

def cargar_datos():

    global siguiente_id, tareas

    try:

        with open('tareas.json', 'r') as f:

            data = json.load(f)

            tareas = data['tareas']

            siguiente_id = data['siguiente_id']

    except FileNotFoundError:

        pass
@bp.get("/")
def index():
    return render_template("index.html", tareas=listar_tareas())


@bp.post("/tareas/agregar")
def post_agregar():
    agregar_tarea(request.form.get("texto", ""))
    return redirect(url_for("main.index"))


@bp.post("/tareas/<int:tarea_id>/completar")
def post_completar(tarea_id: int):
    completar_tarea(tarea_id)
    return redirect(url_for("main.index"))

