# Calcule el perímetro y la superficie de un triangulo solicitando al 
# usuario la longitud de sus lados. 
import math
import os
os.system('cls')

def calcularPerimetroSuperficie(ladoA, ladoB, ladoC):
    perimetro = ladoA + ladoB +ladoC
    s = perimetro / 2  # Semiperímetro
    superficie = math.sqrt(s * (s - ladoA) * (s - ladoB) * (s - ladoC))  # Fórmula de Herón
    print(f"El perimetro del triangulo es {perimetro} y la superficie es {round(superficie, 2)}")

ladoA = float(input("Ingrese el lado a: "))
ladoB = float(input("Ingrese el lado b: "))
ladoC = float(input("Ingrese el lado c: "))
calcularPerimetroSuperficie(ladoA, ladoB, ladoC)