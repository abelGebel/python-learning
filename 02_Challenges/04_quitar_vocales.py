import os
os.system('cls')
"""
Enunciado
Cree una funcion que tome una cadena y devuelva otra cadena sin todas la vocales.
"""

def delete_vocals(abc):

    # Inicializamos una cadena vacía para almacenar el resultado
    resultado = ""

    # Recorremos cada carácter en la cadena de entrada
    for caracter in abc:
        # Si el carácter no es una vocal, lo agregamos al resultado
        if caracter.lower() not in "aeiou":
            resultado += caracter

    # Retornamos la cadena resultante sin vocales
    return resultado



my_string = delete_vocals("python lenguage")
print(my_string)