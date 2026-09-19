def bubble_sort(lista):

    # Creamos una copia para no modificar la lista original.
    lista = lista[:]

    # Repetimos varias pasadas.
    for i in range(len(lista)):

        # Indicamos si hubo algún intercambio.
        #Si terminamos de revisar y nunca tuvimos que 
        # cambiar de lugar ningún número, el código se detiene inmediatamente 
        intercambio = False

        # Recorremos los elementos vecinos.
        
        # Cada pasada coloca un elemento
        # en su posición final.
        
        #Crea un bucle que define qué 
        # posiciones (índices j) de la lista vamos a revisar en esta pasada.
        for j in range(
            0,
            len(lista) - i - 1
        ):

          
            #Compara el número de la posición actual (j) con el número que tiene justo a la derecha (j + 1).
            if lista[j] > lista[j + 1]:

                # Intercambiamos ambos elementos.
                #Intercambia los dos números de posición simultáneamente. 
                # variables sin necesidad de usar una tercera variable temporal.
                lista[j], lista[j + 1] = (
                    lista[j + 1],
                    lista[j]
                )

                # Indicamos que hubo intercambio.
                intercambio = True

        # Si no hubo intercambios,
        # significa que ya está ordenada.
        if not intercambio:
            break

    # Regresamos la lista ordenada.
    return lista


print(
    bubble_sort(
        [5, 3, 8, 4, 2]
    )
)

