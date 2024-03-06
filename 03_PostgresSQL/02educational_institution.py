"""
CE: Mediante un menú de opciones realizar el siguiente programa modular para gestionar el listado de
notas de un examen para los alumnos de una institución educativa:

a. Registrar alumnos: para cada uno se debe solicitar DNI, nombre y nota. Validar que la nota se
encuentre entre 0 y 10. El proceso finaliza cuando se ingresa un DNI igual a cero.

b. Mostrar el listado de alumnos con sus respectivas notas.

c. Buscar a un alumno por su DNI y mostrar su nombre y nota.

d. Ordenar la lista de alumnos en forma ascendente por nombre. 

Gestionar el listado de notas utilizando una base de datos.
"""

import os
import psycopg2

def verificarOpcion():
    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            if op < 1 or op >5:
                print ("ERROR. Intentelo nuevamente...")
            else:
                break    
        except:
            print("ERROR. Intentelo nuevamente...")
    return op

def menu():
    print("1) Registrar alumnos")
    print("2) Mostrar listado de alumnos")
    print("3) Buscar alumno por DNI")
    print("4) Ordenar alumnos de forma ascendente por nombre")
    print("5) Salir")
    print("")
    opcion= verificarOpcion()
    return opcion

def verificarDNI():
    while True:
        try:
            dni = int(input("DNI: ")) 
            if dni >= 0:
                break  
            else:
                print("ERROR. Intente nuevamente...")  
        except:
            print("ERROR. Intente nuevamente...")    
    return str(dni)

def verificarNombre():
    while True:
        nombre = input('Nombre: ')
        if nombre == '' or nombre.replace(' ','').isalpha()==False:
            print("ERROR. Intente nuevamente...")
        else:
            break      
    return nombre

def verificarNota():
    while True:
        try:
            nota = int(input("Nota: "))
            if nota<0 or nota>10:
                print("ERROR. Intentelo nuevamente...")
            else:
                break

        except:
            print("ERROR. Intentelo nuevamente...")

    return nota

def registrar():
    os.system('cls')
    while True:
        os.system('cls')
        print("")
        print("----------REGISTRO DE ALUMNOS----------")
        print("---(Ingrese un dni = 0 para finalizar)---")
        print("")

        dni = verificarDNI()
        if dni == '0':
            break
        nombre = verificarNombre()
        nota= verificarNota()

        cursor = connection.cursor()

        # Definir la consulta SQL para actualizar el registro en la tabla
        sql_insert = """INSERT INTO alumno (dni, nombre, nota) VALUES (%s, %s, %s)"""

        # Ejecutar la consulta SQL con los valores proporcionados
        cursor.execute(sql_insert, (dni, nombre, nota))
        # Confirmar la transacción
        connection.commit()
        cursor.close()

        print("Alumno agregado correctamente")
        continuar = input("(ENTER para continuar)")
        print("")


def mostrar():
    os.system('cls')
    print("")
    print("LISTADO DE ALUMNOS")
    print("")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alumno")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

    print("")
    continuar = input("(ENTER para continuar)")
    print("")


def buscar():
    os.system('cls')
    dni = verificarDNI()
    encontrado = False

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alumno")
    rows = cursor.fetchall()
    cont = 0
    for row in rows:
        if row[0] == dni:
            print(row)
            encontrado = True
            break
        cont += 1
    cursor.close()

    if not(encontrado):
        print("Dni no registrado")

    print("")
    continuar = input("(ENTER para continuar)")
    print("")

def ordenar():

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alumno ORDER BY nombre ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

    print("")
    continuar = input("(ENTER para continuar)")
    print("")

#Principal

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'abel2023Fiunju123',
        database = 'my_database'
    )
except Exception as ex:
    print(ex)


os.system('cls')
opcion = 0
while opcion != 5:
    os.system('cls')
    opcion  = menu()
    if opcion == 1:
        alumnos= registrar()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        buscar()
    elif opcion == 4:
        ordenar()

print("")
os.system('cls')
print("Fin programa")
connection.close()
