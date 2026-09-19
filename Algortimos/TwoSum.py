#two sum
def two_sum(lista, target):

    # Diccionario donde guardaremos:
    # número → índice
    vistos = {}

    # enumerate() nos da:
    # índice
    # valor
    for indice, numero in enumerate(lista):

        # Calculamos cuánto nos falta
        # para llegar al target.
        complemento = target - numero

        # ¿Ya vimos ese número?
        if complemento in vistos:

            # Si sí, regresamos ambos índices.
            return [
                vistos[complemento],
                indice
            ]

        # Si todavía no existe,
        # guardamos el número y su índice.
        vistos[numero] = indice

    # Si no encontramos ninguna combinación,
    # devolvemos una lista vacía.
    return []


print(two_sum([2, 11, 7, 15], 9))
