# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math
import os
os.system('cls')

def calcularHipotenusa(catetoA, catetoB):
    hipotenusa = math.sqrt(catetoA**2 + catetoB**2)
    return hipotenusa

catetoA = float(input("Ingrese el primer cateto: "))
catetoB = float(input("Ingrese el segundo cateto: "))
hipotenusa = calcularHipotenusa(catetoA, catetoB)
print(f"El valor de la hipotenusa es: {round(hipotenusa, 2)}")