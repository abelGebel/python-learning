# Calcule el resultado de las siguientes expresiones algebraicas y muestre los 
# valores resultantes de A y B.
# A = X + (5/2)*X - 4
# B = (30 / (Z-1) * (Z-2)**2) * 4

import os
os.system('cls')

def calcularExpresionesAlgebraicas(valorX, valorZ):
    A = valorX + (5/2)*valorX - 4
    print(f"El valor de la expresion A = X + (5/2)*X - 4 con X = {valorX} es {round(A,2)}")
    try:
        B = (30 / (valorZ-1) * (valorZ-2)**2) * 4
        print(f"El valor de la expresion B = (30 / (Z-1) * (Z-2)**2) * 4 con Z = {valorZ} es {round(B,2)}")
    except ZeroDivisionError:
        print("ERROR: DIVISION POR CERO")

valorX = float(input("Ingrese el valor de X: "))
valorZ = float(input("Ingrese el valor de Z: "))
calcularExpresionesAlgebraicas(valorX, valorZ)
