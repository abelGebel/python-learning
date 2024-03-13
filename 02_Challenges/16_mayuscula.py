"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
import os
os.system('cls')

def mayuscula(cadena:str):
    array = cadena.split()
    salida = ""
    for palabra in array:
        salida += palabra.capitalize() + " "

    print(salida)

mayuscula("una cadena de texto")