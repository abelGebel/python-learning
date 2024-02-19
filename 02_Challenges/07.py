import os
os.system('cls')
"""
Enunciado:
Dado una lista ordenada, se pide que se busque un  elemento especifico de manera optima 
(la lista debe permanecer ordenada).
"""

def busqueda_binaria(lista, x):

    """
    Función que realiza una búsqueda binaria en una lista ordenada para encontrar
    el índice de un elemento dado x. Devuelve el índice si se encuentra el elemento,
    de lo contrario devuelve -1.
    
    Args:
    - lista: Una lista ordenada de elementos.
    - x: El elemento a buscar en la lista.
    
    Returns:
    - El índice del elemento x en la lista, o -1 si no se encuentra.
    """

    izq = 0  # Índice izquierdo de la sublista actual.
    der = len(lista) - 1  # Índice derecho de la sublista actual.

    while izq <= der:
        medio = (izq + der) // 2  # Índice medio de la sublista actual.
        print("izq:", izq, "der:", der, "medio:", medio)

        if lista[medio] == x:  # Si el elemento medio es igual a x, lo hemos encontrado.
            return medio
        elif lista[medio] > x:  # Si el elemento medio es mayor que x, buscamos en la mitad izquierda.
            der = medio - 1
        else:  # Si el elemento medio es menor que x, buscamos en la mitad derecha.
            izq = medio + 1

    # Si llegamos acá, significa que x no está en la lista.
    return -1


lista = [2, 3, 44, 45, 90, 92, 100, 178, 200, 203]
valor = int(input("¿Valor buscado?: "))

print ('El elemento se encuentra en la posicion', busqueda_binaria(lista, valor))

