"""
Define una función pura llamada sin_duplicados con la siguiente signatura:
sin_duplicados(a: list) -> list
que reciba una lista y devuelva una lista nueva sin elementos repetidos,
conservando el orden de la primera aparición de cada elemento.

Ejemplo:
>>> sin_duplicados([1, 2, 2, 3, 1, 4])
[1, 2, 3, 4]
>>> sin_duplicados([])
[]
"""



"""
Define una función pura llamada rotar con la siguiente signatura:
rotar(a: list, n: int) -> list
que devuelva una lista nueva con los elementos de a rotados n posiciones
hacia la izquierda. Si n es negativo, la rotación es hacia la derecha.
Si n es mayor que la longitud de la lista, se sigue rotando de forma cíclica.

Ejemplo:
>>> rotar([1, 2, 3, 4, 5], 2)
[3, 4, 5, 1, 2]
>>> rotar([1, 2, 3, 4, 5], -1)
[5, 1, 2, 3, 4]
>>> rotar([1, 2, 3], 7)
[2, 3, 1]
"""



"""
Define una función pura llamada particionar con la siguiente signatura:
particionar(a: list, n: int) -> list
que divida la lista a en sublistas de tamaño n y devuelva una lista de listas.
La última sublista puede tener menos elementos si no alcanzan.

Ejemplo:
>>> particionar([1, 2, 3, 4, 5, 6, 7], 3)
[[1, 2, 3], [4, 5, 6], [7]]
>>> particionar([1, 2, 3, 4], 2)
[[1, 2], [3, 4]]
"""




"""
Define una función pura llamada mezclar_ordenadas con la siguiente signatura:
mezclar_ordenadas(a: list, b: list) -> list
que reciba dos listas ya ordenadas de menor a mayor y devuelva una lista nueva
ordenada con todos los elementos de ambas, sin usar sorted ni sort.

Ejemplo:
>>> mezclar_ordenadas([1, 4, 7], [2, 3, 9])
[1, 2, 3, 4, 7, 9]
>>> mezclar_ordenadas([1, 2], [])
[1, 2]
"""






"""
Define una función pura llamada aplanar con la siguiente signatura:
aplanar(a: list) -> list
que reciba una lista que puede contener otras listas anidadas (a cualquier
profundidad) y devuelva una lista nueva con todos los elementos en un único nivel.

Ejemplo:
>>> aplanar([1, [2, 3], [4, [5, 6]]])
[1, 2, 3, 4, 5, 6]
>>> aplanar([[], [1], [[2]]])
[1, 2]
"""





"""
Define una función pura llamada intercalar_n con la siguiente signatura:
intercalar_n(*listas: list) -> list
que reciba un número cualquiera de listas y devuelva una lista nueva con los
elementos intercalados por turnos. Si alguna lista es más corta, simplemente
se salta cuando se le acaban los elementos.

Ejemplo:
>>> intercalar_n([1, 4], [2, 5], [3, 6])
[1, 2, 3, 4, 5, 6]
>>> intercalar_n([1, 4, 7], [2], [3, 5])
[1, 2, 3, 4, 5, 7]
"""





"""-------x---------"""




def sin_duplicados(a: list) -> list:
    vistos = []
    resultado = []
    for x in a:
        if x not in vistos:
            vistos.append(x)
            resultado.append(x)
    return resultado





def rotar(a: list, n: int) -> list:
    if not a:
        return []
    n = n % len(a)
    return a[n:] + a[:n]





def particionar(a: list, n: int) -> list:
    if n <= 0:
        raise ValueError("n debe ser positivo")
    return [a[i:i + n] for i in range(0, len(a), n)]



def mezclar_ordenadas(a: list, b: list) -> list:
    resultado = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado






def aplanar(a: list) -> list:
    resultado = []
    for x in a:
        if isinstance(x, list):
            resultado.extend(aplanar(x))
        else:
            resultado.append(x)
    return resultado



def intercalar_n(*listas: list) -> list:
    resultado = []
    max_len = max((len(l) for l in listas), default=0)
    for i in range(max_len):
        for lista in listas:
            if i < len(lista):
                resultado.append(lista[i])
    return resultado




"""Bonus: solución del ejercicio original intercalar"""

def intercalar(a: list, b: list) -> list:
    resultado = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            resultado.append(a[i])
        if i < len(b):
            resultado.append(b[i])
    return resultado












































