"""Programa principal que calcula el peso molecular de la insulina.

Este script importa el módulo `jsonFileHandler` para leer un fichero JSON con
información sobre las secuencias de insulina y los pesos de los aminoácidos.
A partir de esos datos, concatena las cadenas de la subunidad B y A,
realiza un conteo de residuos y calcula un peso molecular estimado, comparándolo
con el valor real incluido en el propio JSON.

Uso típico::

    python3 calc_weight_json.py

El fichero JSON deberá residir en el subdirectorio `files/` o en una ruta
proporcionada en la variable `JSON_PATH`.
"""

import jsonFileHandler as jsonFileHandler
from typing import Dict, Any


JSON_PATH = "files/insulin.json"  # ruta relativa al directorio de trabajo (puede cambiarse según la ubicación del JSON)


def main() -> None:
    """Función principal del programa.

    Lee el fichero JSON y, si la lectura es exitosa, extrae los datos
    necesarios para el cálculo y despliega los resultados por consola.
    """
    # lectura de datos
    data: Any = jsonFileHandler.readJsonFile(JSON_PATH)

    if data != "":
        # extraer cadenas de insulina
        bInsulin: str = data["molecules"]["bInsulin"]
        aInsulin: str = data["molecules"]["aInsulin"]
        insulin: str = bInsulin + aInsulin
        molecularWeightInsulinActual: float = data.get("molecularWeightInsulinActual", 0.0)

        print(f"bInsulin: {bInsulin}")
        print(f"aInsulin: {aInsulin}")
        print(f"molecularWeightInsulinActual: {molecularWeightInsulinActual}")

        # cálculo del peso molecular aproximado
        # obtener tabla de pesos de aminoácidos y contar apariciones
        aaWeights: Dict[str, float] = data.get("weights", {})
        aaCountInsulin: Dict[str, float] = {
            x: float(insulin.upper().count(x))
            for x in [
                "A", "C", "D", "E", "F", "G", "H", "I", "K", "L",
                "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y",
            ]
        }

        molecularWeightInsulin: float = sum(
            (aaCountInsulin[x] * aaWeights.get(x, 0.0))
            for x in aaCountInsulin
        )

        print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
        if molecularWeightInsulinActual:
            percent_error = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
            print("Percent error: " + str(percent_error))
    else:
        print("Error. Exiting program")


if __name__ == "__main__":
    main()
