# Diseñar un programa que permita calcular la edad de una persona ingresando su 
# año de nacimiento.

import os
from datetime import datetime
os.system('cls')

def calcularEdad(anioNacimiento):
    anioActual = datetime.now().year
    print(f"Su edad es: {anioActual - anioNacimiento}")

anioNacimiento = int(input("Ingrese su anio de nacimiento: "))
calcularEdad(anioNacimiento)