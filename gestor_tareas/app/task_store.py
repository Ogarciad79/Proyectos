from __future__ import annotations

_tareas: list[dict[str, object]] = []
_siguiente_id = 1


def agregar_tarea(texto: str) -> int | None:
    """Añade una tarea con id incremental. Devuelve el id asignado o None si el texto está vacío."""
    global _siguiente_id
    limpio = texto.strip()
    if not limpio:
        return None
    tid = _siguiente_id
    _siguiente_id += 1
    _tareas.append({"id": tid, "texto": limpio, "completada": False})
    return tid
import json

def guardar_datos():

    with open('tareas.json', 'w') as f:

        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f)

def completar_tarea(id: int) -> bool:
    """Marca la tarea con ese id como completada. Devuelve True si existía."""
    for t in _tareas:
        if t["id"] == id:
            t["completada"] = True
            return True
    return False


def listar_tareas() -> list[dict[str, object]]:
    """Copia ordenada: incompletas arriba, completadas abajo; luego por id."""
    return sorted(
        _tareas,
        key=lambda t: (
            bool(t.get("completada", False)),
            int(t.get("id", 0)),
        ),
    )
