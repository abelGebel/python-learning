"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""
import os
os.system('cls')
import re

def eliminar_no_deseados(cadena):
    # Definir la expresión regular para los caracteres no deseados
    patron = r'[^{}[\]()]'
    # Utilizar re.sub para reemplazar los caracteres no deseados por una cadena vacía
    nueva_cadena = re.sub(patron, '', cadena)
    return nueva_cadena

def verificar_delimitacion(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}  # Diccionario para mapear los pares de delimitadores

    for caracter in expresion:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila or pila.pop() != pares[caracter]:
                return False

    return not pila

# Ejemplo de uso
expresion = '(a+b)'

print(verificar_delimitacion(expresion))  # Output: True
