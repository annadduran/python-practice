def selection_sort(lista):

    # Copiamos la lista.
    lista = lista[:]

    # Recorremos cada posición.
    for i in range(len(lista)):

        # Suponemos que el elemento actual
        # es el menor.
        indice_minimo = i

        # Buscamos un elemento menor
        # en la parte restante.
        for j in range(i + 1, len(lista)):

            # Si encontramos uno menor...
            if lista[j] < lista[indice_minimo]:

                # Guardamos su posición.
                indice_minimo = j

        # Intercambiamos el actual
        # con el mínimo encontrado.
        lista[i], lista[indice_minimo] = (
            lista[indice_minimo],
            lista[i]
        )

    return lista


print(
    selection_sort(
        [64, 25, 12, 22, 11]
    )
)
