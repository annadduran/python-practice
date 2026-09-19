def busqueda_lineal(lista, objetivo):

    # enumerate() nos proporciona
    # índice y elemento.
    for indice, elemento in enumerate(lista):

        # Comprobamos si encontramos
        # el elemento que buscamos.
        if elemento == objetivo:

            # Regresamos su posición.
            return indice

    # Si terminamos el ciclo sin encontrarlo,
    # devolvemos -1.
    return -1


print(
    busqueda_lineal(
        [10, 20, 30, 40],
        30
    )
)

