"""
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""

def imprimirCadenas(str1, str2):
    out1 = ""
    out2 = ""
    for caracter in str1:
        if caracter not in str2:
            out1 = out1 + caracter
    
    for caracter in str2:
        if caracter not in str1:
            out2 = out2 + caracter 

    print(f"Out1 = {out1}")
    print(f"Out2 = {out2}")

imprimirCadenas("hola", "hablar")