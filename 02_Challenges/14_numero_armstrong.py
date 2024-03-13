"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 */
Un número de Armstrong, también conocido como número narcisista o número pleno, 
es un número natural que es igual a la suma de sus propios dígitos elevados a una 
potencia igual al número total de dígitos. Por ejemplo, un número de Armstrong de 3 
dígitos es un número en el cual la suma de cada uno de sus dígitos elevado a la tercera 
potencia es igual al número en sí mismo.
"""

def verificarNumArmstrong(num):
    num = str(num)
    acum = 0
    potencia = len(num)
    for digit in num:
        acum = acum + (int(digit))**potencia

    if acum == int(num):
        print(f"El numero {num} es un numero de armstrong.")
    else:
        print(f"El numero {num} NO es un numero de armstrong.")


verificarNumArmstrong(153)
verificarNumArmstrong(100)
verificarNumArmstrong(407)