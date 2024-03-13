"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
  lanzará una excepción.
"""
import os
os.system('cls')
from datetime import datetime

def diferencia_entre_fechas(fecha1, fecha2):
    # Convertir las cadenas de texto en objetos de fecha
    try:
        fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Una o ambas fechas no tienen el formato correcto")

    # Calcular la diferencia en días
    diferencia = abs(fecha1 - fecha2)

    # Retornar el número de días como un entero
    return diferencia.days

# Ejemplo de uso
fecha1 = "01/01/2023"
fecha2 = "05/09/2023"
print(diferencia_entre_fechas(fecha1, fecha2))  # Salida: 4