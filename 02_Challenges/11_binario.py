"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""
import os
os.system('cls')

decimal = 20
binario = bin(decimal)
print("El número decimal", decimal, "en binario es:", binario)

decimal = 20
binario = format(decimal, 'b')
print("El número decimal", decimal, "en binario es:", binario)