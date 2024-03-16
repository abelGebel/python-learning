"""Diseñe un algoritmo que permita calcular las raíces de una ecuación de 
segundo grado cuya fórmula es la indicada a continuación. 
Debe indicar todos los casos posibles incluyendo las raíces imaginarias."""
import os
os.system('cls')
import cmath

def calcularRaices(a, b, c):
    discriminante = b**2 - 4*a*c
    raiz_1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    raiz_2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    
    if raiz_1.imag == 0j:
        raiz_1 = float(raiz_1.real)
        raiz_1 = round(raiz_1, 2)
    else:
        raiz_1 = complex(round(raiz_1.real, 2), round(raiz_1.imag, 2))

    if raiz_2.imag == 0j:
        raiz_2 = float(raiz_2.real)
        raiz_2 = round(raiz_2, 2)
    else:
        raiz_2 = complex(round(raiz_2.real, 2), round(raiz_2.imag, 2))

    print(f"x0 = {raiz_1}")
    print(f"x1 = {raiz_2}")

a = float(input("Ingrese el termino a: "))
b = float(input("Ingrese el termino b: "))
c = float(input("Ingrese el termino c: "))

calcularRaices(a, b, c)