"""Diseñe un algoritmo para solicitar ultimo dígito del documento de una persona e 
informe si cobra por cajero o por ventanilla, dependiendo si este valor es par 
o impar respectivamente. Considere al cero dentro del conjunto de los pares."""

import os
os.system('cls')

def verificarParidadDni(ultimoDigito):
    if ultimoDigito % 2 == 0:
        print("Terminacion par, cobra por cajero.")
    else:
        print("Terminacion impar, cobra por ventanilla.")

ultimoDigito = int(input("Ingrese el ultimo digito de su dni: "))
verificarParidadDni(ultimoDigito)