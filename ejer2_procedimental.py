def cuadrado(n: int) -> None:
    """Imprime un cuadrado con el número de líneas indicado."""
    i = 0
    while i < n:
        print('*' * n  )
        i += 1

def cuadrado(n: int) -> None:
    def aux(filas: int) -> None:
        if filas == 0:
            return
        aux(filas - 1)
        print('*' * n)


def diagonal(n: int) -> None:
    """Imprime una línea diagonal con el número de asteriscos indicado."""
    i = 1
    while i <= n:
        print(' ' * i + '*', sep='')
        i += 1