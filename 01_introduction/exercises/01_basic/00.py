import math, os
os.system('cls')
# 1. Calcular el volumen de una esfera cuya fórmula es: V = 4/3*pi*r^3 

def calcularVolumenEsfera(r):
    vol = (4/3)*math.pi*r**3 
    return vol

#radio = float(input("Ingrese el radio de la esfera: "))
#volumen = round(calcularVolumenEsfera(radio), 2)
#print(f"El volumen de la esfera con el radio ingresado es: {volumen}")

# 2. En base a la edad de una persona determinar si es mayor de edad o no.

def esMayor(edad):
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Usted no es mayor de edad.")

#edad = int(input("Ingrese su edad: "))
#esMayor(edad)


# 3. Calcule el valor de Y siempre que sea posible, en caso contrario emita un   
#    mensaje informando. Y = 2*A/(B-C)

def calcularY(valorA, valorB, valorC):
    
    try:
        Y = 2*valorA/(valorB-valorC)
        print(f"El valor de la expresion Y = 2*A/(B-C) es: {round(Y,2)}")
    except ZeroDivisionError:
        print("ERROR: DIVISION POR CERO")
    
#valorA = float(input("Ingrese el valor A: "))
#valorB = float(input("Ingrese el valor B: "))
#valorC = float(input("Ingrese el valor C: "))

#calcularY(valorA, valorB, valorC)



# 4. Dados el precio de un producto y el número de unidades a comprar determine el 
#    importe de dinero a pagar. Considere, además que a partir de las 5 unidades se 
#    realiza un descuento del 10% sobre el total de la compra.


def calcularImporte(precio, cantidad):
    total = precio * cantidad
    if cantidad >= 5:
        total = total - total * 0.10
        print("Se aplico un descuento del %10 sobre el total.")
    return total

precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))
total = calcularImporte(precio, cantidad)

print(f"El importe de dinero a pagar es: ${round(total,2)}")
