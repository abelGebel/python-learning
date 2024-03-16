# Diseñar un programa que permita calcular el índice de masa corporal de una persona.
import os
os.system('cls')

def calcularIndiceCorporal(peso, altura):
    indice = peso / (altura**2)
    print(f"Su indice de masa muscular es: {indice}")

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros:"))
calcularIndiceCorporal(peso, altura)