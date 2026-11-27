def normalizar(nombres) 

"""
Normaliza nombres.

Recibe una lista de cadenas con posiles espacios extra y que mezcla incorrectamente mayúsculas y minúsculas, y devuelve una lista con los nombres normalizados:

- Elimina espacios iniciales y finales.
- Sustituye varios espacios internos consecutivos por uno solo.
- Pone la inicial de cada palabra en ayúsculas y el resto en minúsculas.

>>> normalizar_nombres(["   ana     LópEz", "JOSE    PÉREZ "])
["Ana López", "José Pérez"]
"""

def limpiar(nombre: str) -> str:

    res  = []
    i = 0
    while i < len(nombres):
        res.append(limpiar(nombres[i]))
        i += 1
    return res