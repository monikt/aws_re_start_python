"""Módulo auxiliar para leer documentos JSON.

Provee una única función de conveniencia que abre un fichero, intenta parsearlo y
devolver el contenido convertido en tipos de Python (normalmente un dict).

Este módulo puede importarse desde otros scripts y programas.
"""

import json
from typing import Any


def readJsonFile(fileName: str) -> Any:
    """Lee un fichero JSON y devuelve su contenido.

    Si el fichero no puede abrirse, la función atrapa el error y devuelve una
    cadena vacía. Se recomienda comprobar el valor devuelto antes de usarlo.

    Args:
        fileName: ruta al fichero JSON.

    Returns:
        El contenido del JSON convertido a tipos Python (dict/Lista/etc.) o
        cadena vacía si ocurrió un problema al abrir/leer el fichero.
    """
    data: Any = ""
    try:
        with open(fileName, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except IOError:
        # El mensaje se escribe en stderr para que pueda capturarse si el
        # llamador lo desea.
        print("Could not read file")
    return data
