def insertion_sort(lista):

    lista = lista[:]

    # Comenzamos desde el segundo elemento.
    # porque una lista con un solo elemento (el índice 0) ya está técnicamente ordenada.
    for i in range(1, len(lista)):

        # Guardamos el elemento actual.
        actual = lista[i]

        # Empezamos a revisar
        # desde el elemento anterior.
        
        
        #Creamos una variable j que apunta a la caja que está justo a la izquierda de la que acabamos de sacar.
        j = i - 1

        # Mientras no salgamos de la lista
        # y el elemento anterior sea mayor...
        while (
            j >= 0
            and lista[j] > actual
        ):

            # Movemos el elemento hacia la derecha.
            lista[j + 1] = lista[j]

            # Retrocedemos.
            #Seguir revisando hacia atras
            j -= 1

        # Colocamos el elemento
        # en la posición correcta.
        lista[j + 1] = actual

    return lista


print(
    insertion_sort(
        [5, 2, 4, 6, 1, 3]
    )
)

