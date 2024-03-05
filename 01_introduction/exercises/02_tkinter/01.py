"""Diseñe un programa que dados los números A y B permita realizar las siguientes 
operaciones a elección del operador.
a. Calcular la raíz cuadrada de A
b. Producto de A y B
c. Cociente entre A y B
d. Fin del programa"""

import os, math
os.system('cls')

def menu():
    print("a. Calcular la raíz cuadrada de A")
    print("b. Producto de A y B")
    print("c. Cociente entre A y B")
    print("d. Fin del programa")

    opcion = input("Ingrese una opcion: ")
    return opcion

def calcularRaizA():
    try:
        A = float(input("Ingrese el valor de A: "))   
        raiz = math.sqrt(A)
        print(f"La raiz cuadrada de {A} es {round(raiz, 2)}")
    except ValueError:
        print("ERROR EN EL VALOR INGRESADO")
    print()
    continuar = input("(ENTER para continuar)")


def calcularPropductoAB():
    A = float(input("Ingrese el valor de A: "))
    B = float(input("Ingrese el valor de B: "))
    producto = A*B
    print(f"El producto entre {A} y {B} es: {round(producto, 2)}")
    print()
    continuar = input("(ENTER para continuar)")


def calcularCocienteAB():
    A = float(input("Ingrese el valor de A: "))
    B = float(input("Ingrese el valor de B: "))
    try:
        cociente = A/B
        print(f"El cociente entre {A} y {B} es: {round(cociente, 2)}")
    except ZeroDivisionError:
        print("ERROR: DIVISION POR CERO")
    
    print()
    continuar = input("(ENTER para continuar)")


opcion = 0
while(True):
    opcion = menu()
    if opcion == 'a':
        calcularRaizA()
    elif opcion == 'b':
        calcularPropductoAB()
    elif opcion == 'c':
        calcularCocienteAB()
    else:
        print()
        print("Fin programa")
        break