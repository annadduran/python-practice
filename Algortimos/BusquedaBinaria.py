def busqueda_binaria(lista, objetivo):

    # Límite izquierdo.
    izquierda = 0

    # Límite derecho.
    derecha = len(lista) - 1

    # Mientras todavía exista
    # un rango válido...
    while izquierda <= derecha:

        # Calculamos el punto medio.
        medio = (izquierda + derecha) // 2

        # Si encontramos el objetivo,
        # devolvemos su índice.
        if lista[medio] == objetivo:
            return medio

        # Si el elemento del medio
        # es menor que nuestro objetivo...
        if lista[medio] < objetivo:

            # Eliminamos la mitad izquierda.
            izquierda = medio + 1

        else:

            # Eliminamos la mitad derecha.
            derecha = medio - 1

    # No encontramos el elemento.
    return -1


print(
    busqueda_binaria(
        [1, 3, 5, 7, 9, 11],
        7
    )
)
