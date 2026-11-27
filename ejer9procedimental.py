"""
Escribir una función disparar(tablero, fila, columna) que reciba una matriz 2D
(lista de listas) que representa un tablero de Hundir la Flota, donde:
"~" es agua.
"B" es un barco.

"X" es barco tocado y "O" es un disparo fallido (agua en la que se ha disparado
previamente).
La función debe comprobar las coordenadas, de forma que:
Si están fuera de los límites del tablero, imprime "Coordenada incorrecta".
Si hay "B", lo cambia a "X" e imprime "¡Tocado!".
Si hay "~", lo cambia a "O" e imprime "Agua". Si ya se había disparado ahí ("X" o "O"), imprime "Ya disparaste aquí"
"""

def disparar(tablero, fila, columna):

    if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero[fila]):
        print("Coordenada incorrecta")

    elif tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"
        print("¡Tocado!")

    elif tablero[fila][columna] == "~":
        tablero[fila][columna] = "O"
        print("Agua")

    else:
        print("Ya disparaste aquí")