"""
Enunciado:
Dada una lista de 1000000 de elementos, extraer uno a uno los primetor 100000 elementos 
praa un posterior analisis en menos de 1 segundo.
"""

import time
from collections import deque # Estructura de datos en Python que representa una cola doblemente terminada.

lista = [0]*1000000 # Crea una lista que contiene un millón de elementos, todos inicializados con el valor 0.
start_time  = time.time()
my_deque = deque(lista) 

#for i in range(len(lista)): 
#    lista.pop(0)               Esta solucion utilizando listas normales no es lo suficientemente eficiente.


for i in range(len(lista)):
    my_deque.pop()

end_time = time.time()
print("Tiempo transcurrido: {:.2f} segundos".format(round(end_time - start_time, 2)))


"""
Deque está optimizado para la inserción y eliminación eficiente tanto al principio 
como al final de la cola. Internamente, deque utiliza una estructura de datos de 
doble enlace, lo que permite eliminar elementos al principio de la cola sin necesidad 
de mover todos los elementos restantes.
"""