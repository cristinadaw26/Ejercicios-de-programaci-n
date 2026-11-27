def eliminar_duplicados(lista: list) -> None:
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[j]  == lista[i]:
                del lista[j]
            else:
                j += 1
        i += 1

def eliminar_duplicados_consecutivos(lista: list) -> None:
    i = 0
    while i < len(lista) - 1:
        if lista[i] == lista[i + 1]:
            del lista