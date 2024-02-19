import os
os.system('cls')
"""
Enunciado:
Otener la cantidad de digitos de un numero entero (int) sin cambiar el timpo de dato.
"""

def cont_digits(number):
    cont = 1

    while number / 10 > 1:
        number = number / 10
        cont = cont + 1
    return cont

num = 39090

print(cont_digits(num))
