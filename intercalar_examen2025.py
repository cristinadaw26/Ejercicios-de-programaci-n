"""
Define una función pura llamada intercalar con la siguiente signatura:
intercalar(a: list, b: list) -> list
que reciba dos listas y devuelva una lista nueva con los elementos intercalados, es decir:
intercalar([a1, a2, ....], [b1, b2, ....]) => [a1,b1,a2,b2,....]
si una lista es más larga que la otra, los elementos sobrantes deben añadirse al final.
Ejemplo:

>>> intercalar([1,3,5],[2,4,6])
>>> [1,2,3,4,5,6]
>>> intercalar([1,3], [2,4,6])
[1,2,3,4,6]
"""

def intercalar(a: list, b: list) -> list:
    n =  min(len(a), len(b))
    return list