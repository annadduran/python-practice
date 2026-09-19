def merge_sort(lista):
    # caso base: Si la lista tiene 0 o 1 elementos, ya no se puede dividir
    # y significa que ya está ordenada, por lo que se retorna tal cual.
    if len(lista) <= 1:
        return lista

    # division: Encontramos el índice medio para partir la lista en dos.
    medio = len(lista) // 2

    # RECURSIÓN IZQUIERDA: Cortamos la primera mitad y la mandamos a ordenar.
    # El resultado ordenado se guarda en la variable 'izquierda'.
    izquierda = merge_sort(lista[:medio])

    # RECURSIÓN DERECHA: Cortamos la segunda mitad y la mandamos a ordenar.
    # El resultado ordenado se guarda en la variable 'derecha'.
    derecha = merge_sort(lista[medio:])

    # COMBINACIÓN: Llamamos a nuestra función interna para fusionar
    # ambas mitades ya ordenadas y retornamos el resultado final.
    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    # Esta lista temporal almacenará los elementos en el orden correcto.
    resultado = []

    # Índices (punteros) para saber en qué posición vamos de cada lista.
    i = 0  # Controla la lista izquierda
    j = 0  # Controla la lista derecha

    # Mientras queden elementos por comparar en AMBAS listas...
    while i < len(izquierda) and j < len(derecha):
        # Comparamos cuál de los dos elementos actuales es menor o igual.
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])  # Añadimos el de la izquierda.
            i += 1  # Avanzamos el puntero de la izquierda.
        else:
            resultado.append(derecha[j])    # Añadimos el de la derecha.
            j += 1  # Avanzamos el puntero de la derecha.

    #  Si la lista derecha se terminó primero,
    # vaciamos todo lo que haya quedado pendiente en la lista izquierda.
    resultado.extend(izquierda[i:])

    # Si la lista izquierda se terminó primero,
    # vaciamos todo lo que haya quedado pendiente en la lista derecha.
    resultado.extend(derecha[j:])

    # Devolvemos la nueva lista completamente ordenada y unificada.
    return resultado

if __name__ == "__main__":
    lista_original = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original:  {lista_original}")
    
    lista_ordenada = merge_sort(lista_original)
    print(f"Lista ordenada:  {lista_ordenada}")
