"""
Debe recibir una lista de tuplas de la forma (valor, cantidad) y devuelve una nueva lista que contenga _cantidad_copias del_valor_original
"""

from typing import Any
def colapsar(lista: list[tuple[Any, int]]) -> list[Any]:
    """
    Devuelve una lista que contiene elementos repetidos según se especifica en las tuplas de la lista original.
   
    Debe recibir una lista de tuplas de la forma (valor, cantidad) y devuelve una nueva lista que contenga _cantidad_copias del_valor_original
    
    >>>  colapsar([(7,3), (2,1)])
    [7,7,7,2]
    >>> colapsar([(1,1),(2,2),(3,3)])
    [1,2,2,3,3,3]
    >>> colapsar([])
    []
    """
    i = 0
    res  = []
    while i < len(lista):
        elem, cant = lista[i]
        #elem = lista[i][0]
        #cant = lista[i][1]
        res  += [elem] * cant
        i += 1
    return res

    def compresion_simple(lista: listy[int]) -> list[tuple[int, int]]:
       
        i = 0
        while i < len(lista):
            elem = lista[i]
            i += 1
