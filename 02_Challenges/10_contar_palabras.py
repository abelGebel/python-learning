"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""


import string

# string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

def contar_palabras(texto):
    # Eliminar signos de puntuación y dividir el texto en palabras
    palabras = texto.translate(str.maketrans('', '', string.punctuation)).lower().split()

    # Crear un diccionario para almacenar el recuento de palabras
    recuento_palabras = {}

    # Contar cuántas veces aparece cada palabra
    for palabra in palabras:
        recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

    # Mostrar el recuento final de todas las palabras
    print("Recuento de palabras:")
    for palabra, recuento in recuento_palabras.items():
        print(f"{palabra}: {recuento}")

# Ejemplo de uso
texto = """
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
Los signos de puntuación no forman parte de la palabra.
Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
No se pueden utilizar funciones propias del lenguaje que
lo resuelvan automáticamente.
"""




contar_palabras(texto)